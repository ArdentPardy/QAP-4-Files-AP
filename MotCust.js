// Purpose: Creating a JavaScript object for Motel customers with attributes and methods
// Author: Ardent Pardy
// Date: 2024-03-25

// Define the MotelCustomer object with attributes and methods
const MotelCustomer = {
  // Customer attributes
  Name: "", // Customer's name
  BirthDate: "", // Customer's birth date
  Gender: "", // Customer's gender
  RoomPreferences: [], // Customer's room preferences (as an array)
  PaymentMethod: "", // Customer's payment method
  MailingAddress: {
    // Customer's mailing address (as a sub-object)
    Street: "", // Street address
    City: "", // City
    State: "", // State
    ZipCode: "", // Zip code
  },
  PhoneNumber: "", // Customer's phone number
  CheckInDate: "", // Customer's check-in date
  CheckOutDate: "", // Customer's check-out date

  // Method to calculate customer's age
  CalculateAge: function () {
    const today = new Date();
    const birthDate = new Date(this.BirthDate);
    let age = today.getFullYear() - birthDate.getFullYear();
    const monthDiff = today.getMonth() - birthDate.getMonth();
    if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
      age--;
    }
    return age;
  },

  // Method to calculate customer's stay duration
  CalculateStayDuration: function () {
    const checkInDate = new Date(this.CheckInDate);
    const checkOutDate = new Date(this.CheckOutDate);
    const timeDiff = Math.abs(checkOutDate.getTime() - checkInDate.getTime());
    const stayDuration = Math.ceil(timeDiff / (1000 * 3600 * 24)); // Convert milliseconds to days
    return stayDuration;
  },

  // Method to generate a customer description
  GenerateCustomerDescription: function () {
    return `Name: ${this.Name}\nAge: ${this.CalculateAge()} years\nGender: ${this.Gender}\nRoom preferences: ${this.RoomPreferences.join(", ")}\nPayment method: ${this.PaymentMethod}\nMailing address: ${this.MailingAddress.Street}, ${this.MailingAddress.City}, ${this.MailingAddress.State}, ${this.MailingAddress.ZipCode}\nPhone number: ${this.PhoneNumber}\nCheck-in date: ${this.CheckInDate}\nCheck-out date: ${this.CheckOutDate}\nStay duration: ${this.CalculateStayDuration()} days`;
  },
};

// Assign values to the attributes of the MotelCustomer object
MotelCustomer.Name = "Rudyard Kipling";
MotelCustomer.BirthDate = "1865-12-30";
MotelCustomer.Gender = "Male";
MotelCustomer.RoomPreferences = ["Non-smoking", "Queen bed"];
MotelCustomer.PaymentMethod = "Credit Card";
MotelCustomer.MailingAddress.Street = "Bateman's";
MotelCustomer.MailingAddress.City = "Burwash";
MotelCustomer.MailingAddress.State = "East Sussex";
MotelCustomer.MailingAddress.ZipCode = "TN19 7DS";
MotelCustomer.PhoneNumber = "+44 1435 882302";
MotelCustomer.CheckInDate = "2024-03-25";
MotelCustomer.CheckOutDate = "2024-03-29";

// Generate a customer description using the GenerateCustomerDescription method
const customerDescription = MotelCustomer.GenerateCustomerDescription();

// Log the customer description to the console
console.log(customerDescription);
