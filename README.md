# Orchid V 2.0

Orchid ingests transaction data from your bank, extends it with customizable data, and serves it through a straightforward, vendor-agnostic API.

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

--------------------------------------------------------

# Normalization Schema

Transfer metadata looks different depending on which bank it comes from. Orchid preserves 100% of the bank's formatting. When data from multiple banks needs to be combined, it passes through the normalizer and is adapted to a universal schema.

```javascript
transaction: {
	UUID: string
	amount: number
	time: number // (unix time)
	type: string // (credit, debit, etc)
	state: string // (authorized, pending, settled, refunded, etc)
	description: string // typically the merchant name
	categories: [string, string, ...]// array of merchant0-side categories
	geodata: {
		???? stuff happens here
		depends what bank geodata loks like
	}
	custom:{
		necessity: number // 1 through 5
		categories: [{string,number}, ...] // see note
		??? This is the "notes" object from v1
	}
}
```

* Note: categories can be split by amount.
For example, you could break up a $5.00 spend like so:

```javascript
categories: [
	{'alcohol':310},
	{'snacks':190}
],
```

The sum of all category amounts must add up to exactly the transaction amount or the write will be rejected.

--------------------------------------------------------

# Mock API

### Transaction Data:

| Name | Abbr. | Type | Description | Returns |
| --- | --- | --- | --- | --- |
| **search** | s | String | Query. Accepts && (and), &#124;&#124; (or), - (not) |  array of txns matching | 
| **merchant** | m | String | Query. Accepts && (and), &#124;&#124; (or), - (not) |  array of txns matching | 
| **location** | l | String | Query. Accepts && (and), &#124;&#124; (or), - (not) |  array of txns matching | 
| **id** | id | String | A single UUID to return |  single transaction object | 

### By Range

| Name | Abbr. | Type | Description | Example | Returns |
| --- | --- | --- | --- | --- | --- |
| **amountrange** | ar |  String | A floor and ceiling for the range. Hypenated numbers. | `1400-24000` is $14.00 - $240.00 | array of txns matching |
| **necessityrange** | nr |  String | Hyphenated floor and ceiling for the range. | `2-5` | array of txns matching |
| **daterange** | dr |  String | A start and end date for the range. Unix timestamps hyphen separated. | `1502691885-1502582094` | array of txns matching |
| **monthbyday** | mbd |  String | A 6 digit month + year | `032016` | day/amount pairs like {01:39924, 02:1914 ... 31:19400} |
| **yearbymonth** | ybm |  String | A year | `2016` | month/amount pairs like {01:39924, 02:1914 ... 31:19400} |
