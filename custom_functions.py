
def custom_function_all(prompt):
    return [
        {
            "name": "extract_film_info_based_on_prompt",
            "description": prompt,
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "Title of the film"
                    },
                    "records": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "date": {
                                    "type": "string",
                                    "description": "Date of the box office record"
                                },
                                "box_office_collection": {
                                    "type": "string",
                                    "description": "Box office collection amount for the given date"
                                },
                                "notes": {
                                    "type": "string",
                                    "description": "Additional notes or records achieved"
                                },
                                "title": {
                                    "type": "string",
                                    "description": "Title of the film"
                                },
                            },
                            "required": ["date", "box_office_collection"]
                        },
                        "description": "Array of records containing box office data and notes for different dates"
                    }
                },
                "required": ["title", "records"]
            }
        }
    ]

def custom_function(prompt):
    return [
        {
            "name": "extract_all_film_info_based_on_prompt",
            "description": prompt,
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "Title of the film"
                    },
                    "records": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "date": {
                                    "type": "string",
                                    "description": "Date of the box office record"
                                },
                                "box_office_collection": {
                                    "type": "string",
                                    "description": "Box office collection amount for the given date"
                                },
                                "title": {
                                    "type": "string",
                                    "description": "Title of the film"
                                },
                            },
                            "required": ["date", "box_office_collection"]
                        },
                        "description": "Array of records containing box office data and dates"
                    }
                },
                "required": ["title", "records"]
            }
        }
    ]