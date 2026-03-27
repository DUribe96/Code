#!/usr/bin/env python3

import csv
import argparse
from collections import defaultdict

def to_int(value):
    return int(value.replace(",", "").strip())

def to_float(value):
    return float(value.replace(",", "").strip())

def read_team_map(filename):
    teams = {}

    with open(filename, newline="", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        header = [h.strip().replace("\ufeff", "").rstrip(",") for h in next(reader)]

        team_id_idx = header.index("TeamId")
        name_idx = header.index("Name")

        for row in reader:
            team_id = to_int(row[team_id_idx])
            team_name = row[name_idx].strip()
            teams[team_id] = team_name

    return teams

def read_product_master(filename):
    products = {}

    with open(filename, newline="", encoding="utf-8-sig") as f:
        reader = csv.reader(f)

        for row in reader:
            product_id = to_int(row[0])
            products[product_id] = {
                "name": row[1].strip(),
                "price": to_float(row[2]),
                "lot_size": to_int(row[3])
            }

    return products


def read_sales(filename):
    sales = []

    with open(filename, newline="", encoding="utf-8-sig") as f:
        reader = csv.reader(f)

        for row in reader:
            sales.append({
                "sale_id": to_int(row[0]),
                "product_id": to_int(row[1]),
                "team_id": to_int(row[2]),
                "quantity": to_int(row[3]),
                "discount": to_float(row[4])
            })

    return sales


def generate_reports(team_map, products, sales,
                     team_report_file, product_report_file):

    team_revenue = defaultdict(float)
    product_stats = defaultdict(lambda: {
        "name": "",
        "gross": 0.0,
        "units": 0,
        "discount_cost": 0.0
    })

    for sale in sales:
        product = products[sale["product_id"]]
        team_name = team_map.get(sale["team_id"], "Unknown")

        units_sold = sale["quantity"] * product["lot_size"]
        gross_revenue = units_sold * product["price"]
        discount_cost = gross_revenue * (sale["discount"] / 100)

        team_revenue[team_name] += gross_revenue

        stats = product_stats[sale["product_id"]]
        stats["name"] = product["name"]
        stats["gross"] += gross_revenue
        stats["units"] += units_sold
        stats["discount_cost"] += discount_cost

    # ---- Team Report ----
    sorted_teams = sorted(
        team_revenue.items(),
        key=lambda x: x[1],
        reverse=True
    )

    with open(team_report_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Team", "GrossRevenue"])
        for team, revenue in sorted_teams:
            writer.writerow([team, f"{revenue:.2f}"])

    # ---- Product Report ----
    sorted_products = sorted(
        product_stats.values(),
        key=lambda x: x["gross"],
        reverse=True
    )

    with open(product_report_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "GrossRevenue", "TotalUnits", "DiscountCost"])
        for p in sorted_products:
            writer.writerow([
                p["name"],
                f"{p['gross']:.2f}",
                p["units"],
                f"{p['discount_cost']:.2f}"
            ])


def main():
    parser = argparse.ArgumentParser(description="Sales Reporting Tool")

    parser.add_argument("-t", "--team-map", required=True)
    parser.add_argument("-p", "--product-master", required=True)
    parser.add_argument("-s", "--sales", required=True)
    parser.add_argument("--team-report", required=True)
    parser.add_argument("--product-report", required=True)

    args = parser.parse_args()

    team_map = read_team_map(args.team_map)
    products = read_product_master(args.product_master)
    sales = read_sales(args.sales)

    generate_reports(
        team_map,
        products,
        sales,
        args.team_report,
        args.product_report
    )


if __name__ == "__main__":
    main()
