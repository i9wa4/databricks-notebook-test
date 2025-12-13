import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    # Hello marimo

    This is a test notebook for marimo.
    """)
    return


@app.cell
def _():
    # ローカルモジュールのインポートテスト
    from common.utils import greet

    message = greet("marimo")
    print(message)
    return (message,)


@app.cell
def _(message):
    # 前のセルの変数を参照
    result = f"Result: {message}"
    result
    return


if __name__ == "__main__":
    app.run()
