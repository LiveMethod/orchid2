# Orchid 2

Orchid ingests transaction data from your bank, extends it with customizable data, and serves it through a straightforward, vendor-agnostic API.

You can learn more about the front and back ends in their respective readmes.

## The Spec

The sequence of Orchid functionality looks like this:

### Authentication

Via user input or stored credentials, Orchid gains permissions to communicate with the target bank's API.

### Scraping

Orchid hits the API collecting transactions for a given window, making sure to overlap with previous scrapes to prevent coverage gaps.

### Response Storage

Store the raw responses, totally unmodified.

### Verification

The newest raw response data is compared against existing data. Old entries are updated where necessary, new entries are appended.

### Raw Transaction Storage

Store verified transactions, with the schema they came with from the bank.

### Normalizer

When data is retrieved, it passes through the Normalizer. This strips the data to core pieces of information dictated by the schema. It also adds the bones for the custom Orchid data.

### Normalized Transaction Storage
Store the normalized, Orchid formatted transactions

### Controller

The controller queries normalized data from storage based on parameters in the API call.

### "Getter" API

The Getter API takes requests via URL and passes them to the controller.

### View

The view consumes the API responses and renders them as a GUI.

### "Setter" API

The setter API takes new data provided by the GUI, and it to storage.

Note: it doesn't go through the normalizer because only custom data (rather than bank data) can be updated on the GUI side, so there's only one schema to begin with.

You can also refer to this diagram:

![Orchid Data Flow](/Spec/Orchid_Flow_02.png?raw=true "Orchid Data Flow")
