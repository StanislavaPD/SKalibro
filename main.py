def instrument_model(data):
    return {
        "description": data.get("description"),
        "invNumber": data.get("invNumber"),
        "serialNumber": data.get("serialNumber"),
        "location": data.get("location"),
        "calibrations": data.get("calibrations", [])
    }