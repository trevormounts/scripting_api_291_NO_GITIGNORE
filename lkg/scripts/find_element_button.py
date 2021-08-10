import logging
import json

log = logging.getLogger(__name__)

def run(context):
    element_info = context.find_element('btn_button')
    json_string = json.dumps(element_info)
    parseable_unicode = json.loads(json_string)
    string_and_variable = 'BUTTON INFO:\n\n' + ' ' + json_string

    print(parseable_unicode['flags']['scrollable'])
    
    # Testing Out Parsing

    # print('====================output find element====================')
    # # print(element_info)

    # print(element_info.text)
    # print(element_info.flags['scrollable'])
    # # print(json_string[0].flags)
    # # print(parseable_unicode)
    # # print(parseable_unicode['width'])
    # print(parseable_unicode)
    # print(parseable_unicode['tag_name'])
    # # print(width)
    # # print(data.width)
    # print('====================end find element====================')


    context.perform_gesture('text_entry_no_submit', 'inp_ta_element_info', string_and_variable)
    context.verify(grep="Button Info")