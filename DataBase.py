# If you have Python and PIP already installed on your system:
# go to the cmd/terminal and use the command: pip install pandas
#                                             pip install openpyxl
import pandas as pd

FIRST_NAME = 'First name'
LAST_NAME = 'Last name'
LOINC_NUM = 'LOINC-NUM'
LOINC_NUM_DIC = 'LOINC_NUM'
TRANSICTION_TIME = 'Transaction time'
VALUE = 'Value'
VALID_START = 'Valid start time'
VALID_STOP = 'Valid stop time'
LOINC_NAME = 'LONG COMMON NAME'
LOINC_NAME_DIC = 'LONG_COMMON_NAME'


class DataBase:
    def __init__(self):
        self._fileData = pd.read_excel('data.xlsx')
        self._loinicDic = pd.read_csv('LoincTable.csv')
        self._fileData = self._fileData.loc[:, ~self._fileData.columns.str.contains('^Unnamed')]

    def print(self):
        print(self._fileData.to_string())

    def search_info(self, first_name, last_name='', loinic_num='', time=''):
        answer = self._fileData.loc[self._fileData[FIRST_NAME] == first_name]
        if last_name != '':
            answer = answer.loc[answer[LAST_NAME] == last_name]
        if loinic_num != '':
            answer = self.__get_loinic(loinic_num, answer)
        answer = answer.loc[answer[TRANSICTION_TIME] <= time]
        return answer

    def get_info(self, first_name, last_name, lonic, date, hour, time):
        answer = self._fileData.loc[(self._fileData[FIRST_NAME] == first_name) &
                                    (self._fileData[LAST_NAME] == last_name) &
                                    (self._fileData[TRANSICTION_TIME] <= time) &
                                    ((self._fileData[VALID_STOP] > time) | (self._fileData[VALID_STOP] == 'none'))]
        answer = self.__get_loinic(lonic, answer)
        if hour == ':':
            answer = answer[(answer[VALID_START] < f"{date} 23:59") &
                            (answer[VALID_START] > f"{date} 00:00")]
            answer[answer[VALID_START] == answer[VALID_START].max()]
            return answer[answer[TRANSICTION_TIME] == answer[TRANSICTION_TIME].max()]
        else:
            answer = answer.loc[answer[VALID_START] == f"{date} {hour}"]
            return answer[answer[TRANSICTION_TIME] == answer[TRANSICTION_TIME].max()]

    def save_data(self):
        self._fileData.to_excel('data.xlsx')

    def get_history(self, first_name, last_name, lonic, from_date, from_hour, to_date, to_hour,
                    time):
        answer = self._fileData.loc[(self._fileData[FIRST_NAME] == first_name) &
                                    (self._fileData[LAST_NAME] == last_name) &
                                    (self._fileData[TRANSICTION_TIME] <= time)]
        answer = self.__get_loinic(lonic, answer)
        if from_date == "--":
            return answer
        if to_date == "--":
            if from_hour == ':':
                return answer.loc[(answer[VALID_START] > f"{from_date} 00:00") &
                                  (answer[VALID_START] < f"{from_date} 23:59")]
            return answer.loc[answer[VALID_START] == f"{from_date} {from_hour}"]
        if to_hour == ':':
            if from_hour == ':':
                return answer.loc[(answer[VALID_START] > f"{from_date} 00:00") &
                                  (answer[VALID_START] < f"{to_date} 23:59")]
            return answer.loc[(answer[VALID_START] > f"{from_date} {from_hour}") &
                                  (answer[VALID_START] < f"{to_date} 23:59")]
        return answer.loc[(answer[VALID_START] > f"{from_date} {from_hour}") &
                                  (answer[VALID_START] < f"{to_date} {to_hour}")]

    def delete_data(self, first_name, last_name, lonic, date, hour, time):  # todo release save
        wanted_data = self.get_info(first_name, last_name, lonic, date, hour, time)
        if wanted_data.empty:
            return False
        self._fileData.at[(self._fileData[FIRST_NAME] == wanted_data[FIRST_NAME].values[0]) &
                          (self._fileData[LAST_NAME] == wanted_data[LAST_NAME].values[0]) &
                          (self._fileData[LOINC_NUM] == wanted_data[LOINC_NUM].values[0]) &
                          (self._fileData[VALID_START] == wanted_data[VALID_START].values[0]) &
                          (self._fileData[VALID_STOP] == wanted_data[VALID_STOP].values[0]) &
                          (self._fileData[TRANSICTION_TIME] == wanted_data[TRANSICTION_TIME].values[
                              0]), VALID_STOP] = time
        self.save_data()
        return True

    def update_data(self, first_name, last_name, lonic, date, hour, new_value, time):  # todo release save
        new_data = self.get_info(first_name, last_name, lonic, date, hour, time)
        if new_data.empty:
            return False
        new_data.at[new_data.index[0], VALUE] = new_value
        new_data.at[new_data.index[0], TRANSICTION_TIME] = time
        self.delete_data(first_name, last_name, lonic, date, hour, time)
        print(new_data.to_string())
        self._fileData = pd.concat([self._fileData, new_data], ignore_index=True)
        self.save_data()
        return True

    def load_data(self, path):
        if path != '':
            data = pd.read_excel(path)
            if not (VALID_STOP in data):
                values = ['none'] * len(data)
                data[VALID_STOP] = values
            if not (LOINC_NAME in data):
                values = []
                index = 0
                for i in data[LOINC_NUM]:
                    values.insert(index, self._loinicDic.loc[self._loinicDic[LOINC_NUM_DIC] == i].iloc[0][LOINC_NAME_DIC])
                    index += 1
                data[LOINC_NAME] = values
            self._fileData = pd.concat([self._fileData, data])
            self.save_data()

    def __get_loinic(self, loinc, df):
        answer = df.loc[df[LOINC_NUM] == loinc]
        if answer.empty:
            name_value = self._loinicDic.loc[self._loinicDic[LOINC_NAME_DIC] == loinc]
            if name_value.empty:
                return answer
            return df.loc[
                df[LOINC_NUM] == name_value.iloc[0][LOINC_NUM_DIC]]
        return answer
