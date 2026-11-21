"""
Course 123, Lecture 1.1:

"""

# 1. Location and time
project_id = "WIND_01"
generation_node_id = "NODE_WIND_01"
settlement_hub_id = "HUB_A"
delivery_start_utc = "2026-12-01T00:00:00+00:00"

# 2. input data.
generation_mwh = 8.0
contract_share = 1.0
#100% of the wind farm's metered electricity generation is covered by the VPPA.
#This 100% coverage applies to every delivery hour during the contract term.

energy_component_usd_per_mwh = 50.0
congestion_component_usd_per_mwh = -15.0
marginal_loss_component_usd_per_mwh = -2.0
hub_price_usd_per_mwh = 50.0
strike_price_usd_per_mwh = 60.0

# 3. Calculate the nodal locational marginal price (LMP).
node_price_usd_per_mwh = (
    energy_component_usd_per_mwh
    + congestion_component_usd_per_mwh
    + marginal_loss_component_usd_per_mwh
)

# 4. Define basis as NODE price minus HUB price.
basis_usd_per_mwh = node_price_usd_per_mwh - hub_price_usd_per_mwh

# 5. Assume all metered generation is sold at the supplied node price.
physical_revenue_usd = generation_mwh * node_price_usd_per_mwh

# 6. Calculate a simple two-way, hub-referenced VPPA settlement.
contracted_generation_mwh = generation_mwh * contract_share
vppa_generator_cashflow_usd = contracted_generation_mwh * (
    strike_price_usd_per_mwh - hub_price_usd_per_mwh
)
vppa_buyer_cashflow_usd = -vppa_generator_cashflow_usd

# 7. Combine the generator's physical revenue and VPPA cash flow.
# This excludes other revenues, costs and contractual adjustments.
combined_generator_revenue_usd = (
    physical_revenue_usd + vppa_generator_cashflow_usd
)

print(f"Project: {project_id}")
print(f"Delivery hour starts: {delivery_start_utc}")
print(f"Generation node: {generation_node_id}")
print(f"Settlement hub: {settlement_hub_id}")
print()
print(f"Node LMP: {node_price_usd_per_mwh:.2f} USD/MWh")
print(f"Hub price: {hub_price_usd_per_mwh:.2f} USD/MWh")
print(f"Node-minus-hub basis: {basis_usd_per_mwh:+.2f} USD/MWh")
print(f"Strike price: {strike_price_usd_per_mwh:.2f} USD/MWh")
print(f"Metered generation: {generation_mwh:.2f} MWh")
print(f"Contracted generation: {contracted_generation_mwh:.2f} MWh")
print()
print(f"Physical revenue: {physical_revenue_usd:.2f} USD")
print(f"Generator VPPA cash flow: {vppa_generator_cashflow_usd:+.2f} USD")
print(f"Buyer VPPA cash flow: {vppa_buyer_cashflow_usd:+.2f} USD")
print(f"Combined generator revenue: {combined_generator_revenue_usd:.2f} USD")