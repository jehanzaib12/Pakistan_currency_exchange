## story_greet
* greet
  - action_greet


# story_Requirements_of_Receiver
* receiver{"requirement_receiver":"Transfer Requirements"}
    - slot{"requirement_receiver":"Transfer Requirements"}
    - action_receiver

# story_Requirements_of_sender
* send{"requirement_send":"Sender Requirement"}
    - slot{"requirement_send":"Sender Requirement"}
    - action_sender
    
# story_Requirements_of_sender_with_greet
* greet
  - action_greet
* send{"requirement_send":"Sender Requirement"}
    - slot{"requirement_send":"Sender Requirement"}
    - action_sender

# story_select_currency
* select_currency_rates{"currency_selector":"Rates of Currency"}
    - slot{"currency_selector":"Rates of Currency"}
    - action_select_currency
    

# story_ask_more
* ask{"ask_more":"I want to ask more"}
   - slot{"ask_more":"I want to ask more"}
   - action_ask_more




    
# story_company_transfer_rates
* transfer_rates{"company_transfer_rates":"Transfer rates"}
   - slot{"company_transfer_rates":"Transfer rates"}
   - action_company_transfer_rates
* goodbye
  - utter_goodbye
* goodbye
  
##story_goodbye
* goodbye
    - utter_goodbye
* goodbye

## story_currency_rate_conversion
* cu_conversion{"ra_conversion":"Currency Conversion"}
    - slot{"ra_conversion":"Currency Conversion"}
    - action_select_first_currency
* select_first_currency{"first_currency_to_conversion":"US Dollar"}
    - slot{"first_currency_to_conversion":"US Dollar"}
    - action_add_first_currency_amount
* rate_first_currency{"first_currency_amount":"100"}
    -  slot{"first_currency_amount":"100"}
    - action_select_second_currency
* select_second_currency{"second_currency_to_conversion":"PKR"}
    - slot{"second_currency_to_conversion":"PKR"}
    - action_calculate_currency_conversion

## story_currency_rate_conversion_with_greet
* greet
    - action_greet
* cu_conversion{"ra_conversion":"Currency Conversion"}
    - slot{"ra_conversion":"Currency Conversion"}
    - action_select_first_currency
* select_first_currency{"first_currency_to_conversion":"US Dollar"}
    - slot{"first_currency_to_conversion":"US Dollar"}
    - action_add_first_currency_amount
* rate_first_currency{"first_currency_amount":"100"}
    -  slot{"first_currency_amount":"100"}
    - action_select_second_currency
* select_second_currency{"second_currency_to_conversion":"PKR"}
    - slot{"second_currency_to_conversion":"PKR"}
    - action_calculate_currency_conversion


## story_greet_duration_of_transfer
* greet
    - action_greet
* transfer_duration{"duration_of_transfer":"duration of transfer"}
    - slot{"duration_of_transfer":"duration of transfer"}
    - action_duration_of_transfer

## story_greet_duration_of_transfer_with_Ask_more
* greet
    - action_greet
* transfer_duration{"duration_of_transfer":"duration of transfer"}
    - slot{"duration_of_transfer":"duration of transfer"}
    - action_duration_of_transfer
* select_currency_rates{"currency_selector":"Currency Rates"}
    - slot{"currency_selector":"Currency Rates"}
    - action_select_currency
    
## story_greet_Requirements_of_sender
* greet
    - action_greet
* sender{"requirement_sender":"Requirements of Sender"}
    - slot{"requirement_sender":"Requirements of Sender"}
    - action_sender

## story_location_in_pakistan
* location{"location_in_pakistan":"Loc in Pakistan"}
   - slot{"location_in_pakistan":"Loc in Pakistan"}
   - action_locations_in_pakistan
* city{"ask_city":"ABBOTTABAD"}
   - slot{"ask_city":"ABBOTTABAD"}
   - action_get_address   

## story_complaint
* do_complaint{"complain":"complaint"}
   - slot{"complain":"complaint"}
   - action_complaint

## story_goodbye
* goodbye
  - utter_goodbye

#story_irrelevant_response
* irrelevant{"irrelevant_response":"i dont know"}
   - slot{"irrelevant_response":"i dont know"}
   - action_irrelevant_response