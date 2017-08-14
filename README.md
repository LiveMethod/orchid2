# Orchid V 2.0

Orchid ingests transaction data from your bank, extends it with customizable data, and serves it through a straightforward, vendor-agnostic API.

## The spec

The sequence of Orchid functionality looks something like this

*[  Authentication  ]*
Via user input or stored credentials, Orchid gains permissions to communicate with the target bank's API.

*[  Scraping  ]*
Orchid hits the API collecting transactions for a given window, making sure to overlap with previous scrapes to prevent coverage gaps.

*[  Verification  ]*
The new data is compared against existing data. Old entries are updated where necessary, new entries are appended.

*[  Storage  ]*
The most recent version(s?) of the data are stored in a nosql database.

*[  Normalizer  ]*
When data is retrieved, it passes through the Normalizer. This strips the data to core pieces of information dictated by the schema.

*[  Controller  ]*
The controller queries normalized data from storage based on parameters in the API call.

*[  "Getter" API  ]*
The Getter API takes requests via URL and passes them to the controller.

*[  View  ]*
The view consumes the API responses and renders them as a GUI.

*[  "Setter" API  ]*
The setter API takes new data provided by the GUI, and passes it through the Normalizer to update storage.


You can also refer to this diagram:

![Orchid Data Flow](/Spec/Orchid_Flow_01.png?raw=true "Orchid Data Flow")