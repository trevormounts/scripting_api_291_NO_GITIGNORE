import logging
import json

log = logging.getLogger(__name__)

def run(context):
    element_info = context.find_element('inp_slider')
    json_string = json.dumps(element_info)
    parseable_unicode = json.loads(json_string)
    
    string_and_variable = 'SLIDER INFO:\n\n' + ' ' + json_string


    context.perform_gesture('text_entry_no_submit', 'inp_ta_element_info', string_and_variable)
    context.verify(grep="SLIDER INFO")