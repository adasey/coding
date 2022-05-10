static_cost, production_cost, price = input().split()
static_cost, production_cost, price = int(static_cost), int(production_cost), int(price)

if price <= production_cost:
    print(-1)

else:
    gain_cost = price - production_cost
    use_cost = static_cost + gain_cost

    benefit_cost = int(use_cost / gain_cost)

    print(benefit_cost)