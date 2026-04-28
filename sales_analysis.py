"""
📊 Sales Data Analysis Project

This script:
✔ Loads sales data from CSV (using full file path)
✔ Explores dataset
✔ Cleans missing values
✔ Performs analysis
✔ Prints a formatted report
"""

import pandas as pd


# -------------------------------
# STEP 1: LOAD DATA
# -------------------------------
def load_data(sales_data):
    """Load CSV file into DataFrame"""
    try:
        df = pd.read_csv(sales_data)
        print(" Data loaded successfully!\n")
        return df
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None


# -------------------------------
# STEP 2: EXPLORE DATA
# -------------------------------
def explore_data(df):
    """Display dataset overview"""
    print(" FIRST 5 ROWS:\n")
    print(df.head(), "\n")

    print(" SHAPE (Rows, Columns):", df.shape, "\n")

    print(" COLUMN NAMES:")
    print(df.columns.tolist(), "\n")

    print("ℹ DATA TYPES:")
    print(df.dtypes, "\n")

    print(" MISSING VALUES:")
    print(df.isnull().sum(), "\n")


# -------------------------------
# STEP 3: CLEAN DATA
# -------------------------------
def clean_data(df):
    """Handle missing values and duplicates"""

    # Fill numeric columns with mean
    num_cols = df.select_dtypes(include=['int64', 'float64']).columns
    df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

    # Fill categorical columns with 'Unknown'
    cat_cols = df.select_dtypes(include=['object']).columns
    df[cat_cols] = df[cat_cols].fillna("Unknown")

    # Remove duplicate rows
    df = df.drop_duplicates()

    print(" Data cleaned successfully!\n")
    return df


# -------------------------------
# STEP 4: ANALYSIS
# -------------------------------
def analyze_data(df):
    """Perform sales analysis"""

    print(" SALES ANALYSIS REPORT\n")

    # Auto-detect column names
    sales_col = None
    product_col = None

    for col in df.columns:
        if "sale" in col.lower():
            sales_col = col
        if "product" in col.lower():
            product_col = col

    # Check if required columns exist
    if sales_col is None or product_col is None:
        print(" Required columns (Product / Sales) not found in dataset")
        return

    # Convert sales column to numeric
    df[sales_col] = pd.to_numeric(df[sales_col], errors='coerce')

    # Calculate metrics
    total_sales = df[sales_col].sum()
    avg_sales = df[sales_col].mean()
    max_sales = df[sales_col].max()

    best_product = df.groupby(product_col)[sales_col].sum().idxmax()

    # Print results
    print(f"💰 Total Revenue: ₹{total_sales:,.2f}")
    print(f"📈 Average Sales: ₹{avg_sales:,.2f}")
    print(f"🔥 Highest Sale: ₹{max_sales:,.2f}")
    print(f"🏆 Best Selling Product: {best_product}")


# -------------------------------
# MAIN FUNCTION
# -------------------------------
def main():
    """
    Main execution function
    NOTE: Using FULL FILE PATH to avoid file not found error
    """

    file_path = r"C:\Users\Gayathri\OneDrive\Desktop\sales_analysis\sales_data.csv"

    df = load_data(file_path)

    if df is not None:
        explore_data(df)
        df = clean_data(df)
        analyze_data(df)


# Run the program
if __name__ == "__main__":
    main()