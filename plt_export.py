import matplotlib.pyplot as plt
import os

def PLTExport(forecast_data):
    os.makedirs("forecast_images", exist_ok=True)
    for model, forecast, item in forecast_data:
        fig = model.plot(forecast)
        plt.title(f"Forecast for '{item}'")
        plt.xlabel("ds")
        plt.ylabel("y")
        plt.tight_layout()

        item = str(item).replace("/", "_").replace("\\", "_").replace(" ", "_")
        file_path = os.path.join("forecast_images", f"{item}.png")

        plt.savefig(file_path, dpi=300)
        plt.close(fig)