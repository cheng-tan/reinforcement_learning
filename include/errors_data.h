//! [Error Definitions]
ERROR_CODE_DEFINITION(1, invalid_argument, "Invalid Argument: ")
ERROR_CODE_DEFINITION(2, background_queue_overflow, "Background queue overflow. ")
ERROR_CODE_DEFINITION(3, eventhub_http_generic, "http error while connecting to event hub. ")
ERROR_CODE_DEFINITION(4, http_bad_status_code, "http request returned a bad status code")
ERROR_CODE_DEFINITION(5, action_not_found, "No actions found in action collection")
ERROR_CODE_DEFINITION(6, background_thread_start, "Unable to start background thread. ")
ERROR_CODE_DEFINITION(7, not_initialized, "")
ERROR_CODE_DEFINITION(8, eventhub_generate_SAS_hash, "")
ERROR_CODE_DEFINITION(9, create_fn_exception, "Create function failed.")
ERROR_CODE_DEFINITION(10, type_not_registered, "Type not registered with class factory")
ERROR_CODE_DEFINITION(11, http_uri_not_provided, "URL parameter was not passed in via configuration")
ERROR_CODE_DEFINITION(12, last_modified_not_found, "Last-Modified http header not found in response")
ERROR_CODE_DEFINITION(13, last_modified_invalid, "Unable to parse Last-Modified http header as date-time")
ERROR_CODE_DEFINITION(14, bad_content_length, "Content-Length header not set or set to zero")
ERROR_CODE_DEFINITION(15, exception_during_http_req, "http request exception. ")
ERROR_CODE_DEFINITION(16, model_export_frequency_not_provided, "Export frequency of model not specified in configuration.")
ERROR_CODE_DEFINITION(17, bad_time_interval, "Bad time interval string.  Format should be hh:mm:ss")
ERROR_CODE_DEFINITION(18, data_callback_exception, "Background data callback threw an exception. ")
ERROR_CODE_DEFINITION(19, data_callback_not_set, "Data callback handler not set")
ERROR_CODE_DEFINITION(20, json_no_actions_found, "Context json did not have actions (_multi array empty or not found)")
ERROR_CODE_DEFINITION(21, json_parse_error, "Unable to parse JSON. ")
ERROR_CODE_DEFINITION(22, exploration_error, "Exploration error code: ")
ERROR_CODE_DEFINITION(23, action_out_of_bounds, "Action id out of bounds.")
ERROR_CODE_DEFINITION(24, model_update_error, "Error updating model: ")
ERROR_CODE_DEFINITION(25, model_rank_error, "Error while ranking actions using model: ")
ERROR_CODE_DEFINITION(26, pdf_sampling_error, "")
ERROR_CODE_DEFINITION(27, eh_connstr_parse_error, "Unable to parse event hub connection string.")
ERROR_CODE_DEFINITION(28, unhandled_background_error_occurred, "A background thread encountered an error but there was no error handler registered. Register an error handler to see the error code and message.")
ERROR_CODE_DEFINITION(29, thread_unresponsive_timeout, "A background thread exceeded the watchdog timer.")
ERROR_CODE_DEFINITION(30, incorrect_buffer_preamble_size, "Buffer preamble is pre-allocated and does not match the size requested.")
ERROR_CODE_DEFINITION(31, serialize_unknown_outcome_type, "Unable to serialize unknown outcome type.")
ERROR_CODE_DEFINITION(32, preamble_error, "Unable to read or write the preamble.")
ERROR_CODE_DEFINITION(33, file_open_error, "Unable to open file.")
ERROR_CODE_DEFINITION(34, json_no_slots_found, "Context json did not have slots (_slots array empty or not found)")
ERROR_CODE_DEFINITION(35, file_read_error, "Unable to read from file.")
ERROR_CODE_DEFINITION(36, file_stats_error, "Unable to read file statistics e.g. modified date time.")
ERROR_CODE_DEFINITION(37, not_supported, "Not supported")
ERROR_CODE_DEFINITION(38, protocol_not_supported, "Protocol version is not supported")
ERROR_CODE_DEFINITION(39, external_error, "Opaque error in external code. ")
ERROR_CODE_DEFINITION(40, unsupported_learning_mode, "Unsupported learning mode")
ERROR_CODE_DEFINITION(41, http_client_init_error, "Cannot initialize http client")
ERROR_CODE_DEFINITION(41, content_encoding_error, "Content encoding should be set to IDENTITY")
//! [Error Definitions]
