import pandas as pd

def analyze_file(file_path):
    """
    Process and analyze the uploaded file.
    """
    try:
        # Load the file
        data = pd.read_csv(file_path)

        # Generate a summary of the dataset
        summary = {
            "shape": data.shape,
            "columns": data.columns.tolist(),
        }

        # Check for the 'type' column and include counts if present
        if 'type' in data.columns:
            wine_counts = data['type'].value_counts().to_dict()
            summary["wine_counts"] = wine_counts
        else:
            summary["wine_counts"] = "Column 'type' not found"

        # Optionally include the first few rows
        summary["head"] = data.head().to_dict(orient="records")

        return {"success": True, "summary": summary}

    except FileNotFoundError:
        return {"success": False, "error": "File not found"}
    except pd.errors.ParserError:
        return {"success": False, "error": "Could not parse the dataset. Please check the file format."}
    except Exception as e:
        return {"success": False, "error": str(e)}
