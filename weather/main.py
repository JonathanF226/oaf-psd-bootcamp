from factory_ds import ServiceFactory
from data_handler import DataServiceHandler

def main():
    """Main function to interact with the user, get the desired service type, and handle the data using the selected service."""
    factory = ServiceFactory()
    service_type = input("Enter service type (mocked/api): ").strip().lower()
    service = factory.get_service(service_type)
    
    if service:
        handler = DataServiceHandler(service)
        try: 
            latitude = float(input("Enter latitude: ").strip())
            longitude = float(input("Enter longitude: ").strip())
        except ValueError:
            print("Invalid latitude or longitude. Please enter numeric values.")
            return
        handler.print_data(latitude, longitude)
    else:
        print("Invalid service type.")

if __name__ == "__main__":
    main()