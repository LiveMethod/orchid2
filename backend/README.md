# Orchid 2 Back End

## Normalization Schema

Transfer metadata looks different depending on which bank it comes from. Orchid preserves 100% of the bank's formatting. When data from multiple banks needs to be combined, it passes through the normalizer and is adapted to a universal schema.

```javascript
transaction: {
	uuid: string
	amount: number
	time: number // (unix time)
	type: string // (credit, debit, etc)
	state: string // (authorized, pending, settled, refunded, etc)
	description: string // typically the merchant name
	categories: [string, string, ...]// array of merchant-side categories
	geodata: { // See note
		city: string,
		state: string, // 2 letter state, caps
		lat: number, // to 5 places, like 38.81602
		lon: number,
		timezone: string, // like "America/New_York"
	}
	custom:{
		necessity: number // 1 through 5
		categories: [{string,number}, ...] // see note
		notes: string // sanitized
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

* Note: geodata is based on simple's until there's more data.

The sum of all category amounts must add up to exactly the transaction amount or the write will be rejected.

--------------------------------------------------------

## Mock API

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

# Running Locally
Enter the local virtual env and start it.
`cd Virtualenvs/orchid && source bin/activate`

Run the database with `make db`
Run the app with `make app`

Leave the virtualenv with `deactivate`

# Additional Resources
Here are some useful links:

[Virtual environments](https://hackercodex.com/guide/python-development-environment-on-mac-osx/)

[Tutorial](https://realpython.com/blog/python/flask-by-example-part-1-project-setup/)

[Flask RESTful](https://flask-restful.readthedocs.io/en/0.3.5/quickstart.html)