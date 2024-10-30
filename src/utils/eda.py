import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def check_df(dataframe: pd.DataFrame) -> None:
    """Browse the dataframe to get a better understanding of its structure.

    Args:
        dataframe (pd.DataFrame): The dataframe to be checked.
    """
    print("##################### Shape #####################")
    print(dataframe.shape)
    print("##################### Types #####################")
    print(dataframe.info(verbose=True))
    print("##################### Head #####################")
    print(dataframe.head(3))
    print("##################### Tail #####################")
    print(dataframe.tail(3))
    print("##################### NA #####################")
    print(dataframe.isnull().sum())
    dataframe = dataframe[[col for col in dataframe.columns if dataframe[col].dtypes != "O"]]
    print("##################### Quantiles #####################")
    print(dataframe.quantile([0, 0.05, 0.50, 0.95, 0.99, 1]).T)
    print("\n")

def grab_col_names(dataframe: pd.DataFrame, cat_th=5, car_th=8) -> tuple:
    """This function returns the list of categorical, numerical, categorical with high cardinality, numerical but categorical columns.

    Args:
        dataframe (pd.DataFrame): the dataframe to be checked.
        cat_th (int, optional): categorical threshold. Defaults to 5.
        car_th (int, optional): cardinality threshold. Defaults to 8.

    Returns:
        tuple: list of categorical columns, list of numerical columns, list of categorical columns with high cardinality, list of numerical columns but categorical.
    """

    cat_cols = [col for col in dataframe.columns if dataframe[col].dtypes == "O"]

    num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < cat_th and
                   dataframe[col].dtypes != "O"]

    cat_but_car = [col for col in dataframe.columns if dataframe[col].nunique() > car_th and
                   dataframe[col].dtypes == "O"]

    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes != "O"]
    num_cols = [col for col in num_cols if col not in num_but_cat]

    print("Observations: {dataframe.shape[0]}".format(dataframe=dataframe))
    print("Variables: {dataframe.shape[1]}".format(dataframe=dataframe))
    print("Categorical Cols: {cat_cols}".format(cat_cols=len(cat_cols)))
    print("Numerical Cols: {num_cols}".format(num_cols=len(num_cols)))
    print("Categorical but Cardinal Cols: {cat_but_car}".format(cat_but_car=len(cat_but_car)))
    print("Numerical but Categotical Cols: {num_but_cat}".format(num_but_cat=len(num_but_cat)))

    return cat_cols, cat_but_car, num_cols, num_but_cat

def cat_summary(dataframe: pd.DataFrame, col_names: list, plot=False) -> None:
    """This function plots the countplot of the categorical variables and prints the value counts and ratios of the categorical variables.

    Args:
        dataframe (pd.DataFrame): dataframe to be checked.
        col_names (list): list of categorical columns.
        plot (bool, optional): If True, it plots the countplot of the categorical variables. Defaults to False.
    """

    num_plots = len(col_names)
    num_cols = len(col_names)
    num_rows = (num_plots + num_cols - 1) // num_cols
    
    if plot:

        fig = make_subplots(rows=num_rows, cols=num_cols, subplot_titles=col_names)

        # Iterate over countplot values
        for i, col_name in enumerate(col_names):
            
            dummy_dataframe = pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)})
            print(dummy_dataframe)

            row = (i // num_cols) + 1
            col = (i % num_cols) + 1
            
            # Add countplot
            fig.add_trace(
                go.Bar(x=dummy_dataframe[col_name].index.values, y=dummy_dataframe[col_name]),
                row=row, col=col
            )

            # Update subplot title
            fig.update_xaxes(row=row, col=col)
            fig.update_yaxes(row=row, col=col)

        # Update layout
        fig.update_layout(
            title='Analysis of Categorical Variables',
            showlegend=False,
            width=1000,
            height=300,
        )

        # Show plot
        fig.show()
    else:
        
        for i, col_name in enumerate(col_names):
            dummy_dataframe = pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)})
            print(dummy_dataframe)
            

def num_summary(dataframe: pd.DataFrame, numerical_col:list, plot=False) -> None:
    """This function prints the descriptive statistics of the numerical variables and plots the histogram of the numerical variables.

    Args:
        dataframe (pd.DataFrame): dataframe to be checked.
        numerical_col (list): list of numerical columns.
        plot (bool, optional): If True, it plots the histogram of the numerical variables. Defaults to False.
    """
    quantiles = [0.05, 0.10, 0.30, 0.50, 0.70, 0.90, 0.99]
    
    if plot:        
        # Calculate subplot rows and columns dynamically
        num_cols = len(numerical_col)
        num_features = len(numerical_col)
        num_rows = (num_features + num_cols - 1) // num_cols

        # Create subplots
        fig = make_subplots(rows=num_rows, cols=num_cols, subplot_titles=numerical_col)
        
        print(dataframe.describe(quantiles))
        # Iterate over subplot rows and columns
        for i, cols in enumerate(numerical_col):

            row = (i // num_cols) + 1
            col = (i % num_cols) + 1

            # Calculate histogram bin range dynamically based on data
            bin_start = dataframe[cols].min()
            bin_end = dataframe[cols].max() + 1
            bin_size = (bin_end - bin_start) / 10  # Adjust the number of bins as needed

            # Add histogram trace
            fig.add_trace(
                go.Histogram(x=dataframe[cols], xbins=dict(start=bin_start, end=bin_end, size=bin_size)),
                row=row, col=col
            )

        # Update layout
        fig.update_layout(
            title='Analysis of Numerical Variables',
            showlegend=False,
            height=300,
            width=800,
        )

        # Show plot
        fig.show()
    
    else:
        print(dataframe.describe(quantiles))
    

def target_summary_with_cat(dataframe: pd.DataFrame, target: str, categorical_col: list) -> None:
    """This function prints the mean of the target variable with respect to the categorical variables.

    Args:
        dataframe (pd.DataFrame): dataframe to be checked.
        target (str): target variable
        categorical_col (list): list of categorical columns.
    """
    df_summary = pd.DataFrame({f"{target}_MEAN": dataframe.groupby(categorical_col)[target].mean()}).sort_values(by=f"{target}_MEAN", ascending=False)
    return df_summary
    