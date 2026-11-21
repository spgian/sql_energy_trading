# Course 123: SQL and Machine Learning for Energy Trading

## Section 1: Building the First Version of the Energy Analytics Model

### Lecture 1.1: Calculating Nodal Prices, Basis and VPPA Cash Flows in Python

This is the first snapshot of one evolving `SQL_Model` application. Later
lectures will extend the same model.

## Files
- `main.py`: the complete runnable application for Lecture 1.1.

All input data is in the clearly marked input block of `main.py`. No external
files are required for this first lesson.

## Run in your project
From the project folder, run:

```bash
python main.py
```
Suggested commit message: `Start one-hour nodal pricing and VPPA model`.

The code uses basic Python 3 syntax and requires no third-party libraries.


## Input data

| Input | Value | Unit or meaning |
| --- | --- | --- |
| project_id | WIND_01 | wind project |
| generation_node_id | NODE_WIND_01 | Generation pricing location |
| settlement_hub_id | HUB_A | VPPA reference location |
| delivery_start_utc | 2026-01-15T12:00:00+00:00 | Start of a one-hour delivery interval |
| energy_component_usd_per_mwh | 50.0 | USD/MWh |
| congestion_component_usd_per_mwh | -15.0 | USD/MWh |
| marginal_loss_component_usd_per_mwh | -2.0 | USD/MWh |
| hub_price_usd_per_mwh | 50.0 | USD/MWh |
| strike_price_usd_per_mwh | 60.0 | USD/MWh |
| generation_mwh | 8.0 | Metered energy for the hour, in MWh |
| contract_share | 1.0 | 100% of metered generation is contracted |

We use a US nodal-pricing framework.

## Technical references

- PJM, Calculation of Day-ahead Prices, including signed LMP components:
  https://agreements.pjm.com/oatt/4476
- PJM Learning Center, Locational Marginal Pricing:
  https://learn.pjm.com/three-priorities/buying-and-selling-energy/lmp.aspx
- US EPA, Financial PPA, including financial settlement directions:
  https://www.epa.gov/green-power-markets/financial-ppa
- RMI, Introduction to the Virtual Power Purchase Agreement, including
  nodal and hub settlement concepts:
  https://rmi.org/wp-content/uploads/2018/12/rmi-brc-intro-vppa.pdf