from calculation import Calculation as calculation
from logger import result_logger as write_log
import data_transformation as d_t
import console as console


def Action():
    j = d_t.data_formatting(console.input_data())
    calculation_result = calculation(j)
    console.view_data(calculation_result, 'Ответ:')
    write_log(j, calculation_result)

Action()