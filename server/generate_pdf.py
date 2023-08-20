from fpdf import FPDF
from generate_gpt import *
from generate_dalle import *
from add_watermark import *
import openai


test_list = ["Welcome to this DIY tutorial on building a self-flying drone station using Arduino! Drones have become increasingly popular in recent years, and their applications range from aerial photography to package delivery. However, one of the challenges with drones is their limited flight time due to battery constraints. This tutorial aims to address this issue by guiding you through the process of creating a self-flying drone station that can autonomously recharge and deploy drones.\n\nThe heart of this project lies in the Arduino platform, which is an open-source electronics platform based on easy-to-use hardware and software. Arduino provides a flexible and accessible way to control various components and sensors, making it an ideal choice for building a self-flying drone station.\n\nIn this tutorial, we will cover all the necessary steps, from gathering the required materials to programming the Arduino board. We will also explore the different components involved, such as the charging dock, drone deployment mechanism, and obstacle detection system.\n\nTo begin, let's discuss the main objectives of this project. The self-flying drone station aims to achieve two primary goals: autonomous recharging and drone deployment. The charging dock will serve as a home base for the drones, where they can land and recharge their batteries automatically. The drone deployment mechanism will enable the station to release drones when needed, allowing them to perform their designated tasks.\n\nTo accomplish these objectives, we will utilize various sensors and actuators. For instance, we will integrate proximity sensors to detect the presence of drones and obstacles, ensuring safe landing and takeoff. Additionally, servo motors will be employed to control the movement of the charging dock and the deployment mechanism.\n\nThroughout this tutorial, we will provide detailed instructions, circuit diagrams, and code snippets to guide you through each step. However, it is important to note that some basic knowledge of electronics and programming will be beneficial. If you are new to Arduino, don't worry! We will explain the concepts and provide resources to help you get started.\n\nBy the end of this tutorial, you will have a fully functional self-flying drone station that can autonomously recharge and deploy drones. This project opens up exciting possibilities for extending the flight time of drones and enabling them to perform tasks without human intervention.\n\nSo, let's dive in and start building your own self-flying drone station using Arduino! Get ready to embark on an exciting journey into the world of autonomous drone technology.", "Before we dive into the materials needed for this project, let's take a moment to appreciate the endless possibilities that drones offer. From aerial photography to package delivery, drones have revolutionized various industries. By building your own drone, you not only gain a deeper understanding of its inner workings but also have the freedom to customize it according to your specific needs.\n\nNow, let's move on to the materials required for this project:\n\n1. Arduino Board: The heart and brain of our drone, the Arduino board will serve as the main controller. It provides the necessary processing power and interfaces with other components. Make sure to choose a compatible Arduino board, such as Arduino Uno or Arduino Nano.\n\n2. Ultrasonic Sensor: This crucial component enables our drone to detect obstacles and measure distances accurately. The ultrasonic sensor emits sound waves and measures the time it takes for them to bounce back, allowing the drone to perceive its surroundings.\n\n3. Motor and Propeller Set: To achieve flight, we need a set of motors and propellers. Look for brushless motors and propellers suitable for your drone's size and weight. Ensure they are compatible with the Arduino board and can be controlled using PWM signals.\n\n4. Electronic Speed Controllers (ESCs): ESCs regulate the speed of each motor based on the input from the Arduino board. Choose ESCs that match the specifications of your motors and provide smooth control.\n\n5. Battery and Power Distribution Board: A reliable power source is essential for our drone's flight. Select a high-capacity LiPo battery that can provide sufficient voltage and current. Additionally, a power distribution board will help distribute power to various components efficiently.\n\n6. Frame and Landing Gear: The drone's frame provides structural support and houses all the components. Look for a lightweight and sturdy frame that suits your design preferences. Landing gear ensures a safe landing and protects the drone during takeoff and landing.\n\n7. Flight Controller: While the Arduino board handles the main control, a flight controller can enhance stability and provide advanced flight features. Consider adding a flight controller like the popular Pixhawk or APM to improve your drone's performance.\n\n8. Miscellaneous Components: Don't forget to gather essential items such as wires, connectors, soldering equipment, a soldering iron, heat shrink tubing, and a screwdriver set. These tools will assist you in assembling and connecting the various components of your drone.\n\nWith these materials at your disposal, you are well on your way to building your very own self-flying drone using Arduino. Remember to stay focused, follow safety precautions, and enjoy the process of bringing your drone to life. Happy building!", "Step 1: Gather the necessary components\nTo begin, gather all the required components for your self-flying drone project. These typically include an Arduino board, a flight controller module, motors, propellers, a power distribution board, a frame, a battery, and various connectors and wires. Ensure you have everything on hand before proceeding.\n\nStep 2: Assemble the frame\nStart by assembling the frame of your drone. Follow the instructions provided with your kit or refer to online resources for guidance. Make sure the frame is sturdy and secure, as it will house all the essential components.\n\nStep 3: Connect the motors and propellers\nAttach the motors to the designated positions on the frame using screws or mounting brackets. Then, connect the propellers to each motor shaft, ensuring they are securely fastened. Take care to follow the correct rotation direction for each propeller, as specified by the manufacturer.\n\nStep 4: Install the flight controller module\nMount the flight controller module onto the frame, ensuring it is positioned at the center of gravity. Secure it firmly using screws or adhesive pads. This module will act as the brain of your drone, controlling its flight and stability.\n\nStep 5: Connect the flight controller to Arduino\nUsing jumper wires, establish the necessary connections between the flight controller module and the Arduino board. Refer to the pinout diagrams provided by the manufacturer to ensure accurate wiring.\n\nStep 6: Power distribution\nConnect the power distribution board to the battery and the flight controller module. This board will distribute power to all the components, ensuring they receive the necessary voltage.\n\nStep 7: Program the Arduino\nWrite or download the appropriate code for your self-flying drone. This code will enable the Arduino to communicate with the flight controller module and control the drone's flight behavior. Upload the code to the Arduino board using the Arduino IDE.\n\nStep 8: Calibrate the drone\nFollow the calibration instructions provided by the flight controller module manufacturer. This step is crucial to ensure accurate sensor readings and stable flight performance.\n\nStep 9: Test and fly\nWith everything connected and calibrated, it's time to test your self-flying drone! Start with a controlled indoor environment, away from obstacles. Gradually increase the complexity of your flights as you gain confidence in your drone's capabilities.\n\nRemember, building a self-flying drone requires patience and attention to detail. Take your time, double-check your connections, and always prioritize safety. Enjoy the process of creating your own autonomous aerial companion and explore the endless possibilities of drone technology!", "1. Safety First: Safety should always be the top priority when building any type of drone. Ensure that you have a good understanding of local regulations and guidelines regarding drone usage. Additionally, take necessary precautions such as using propeller guards, choosing lightweight materials, and performing regular maintenance checks.\n\n2. Selecting the Right Components: Choosing the appropriate components is vital for the functionality and performance of your self-flying drone. Consider factors such as motor power, battery capacity, flight controller capabilities, and sensor accuracy. Research and compare different options to find the best fit for your project.\n\n3. Understanding Flight Dynamics: Familiarize yourself with the principles of flight dynamics, including aerodynamics, thrust, lift, and control mechanisms. This knowledge will help you design and calibrate your drone effectively, ensuring stable and controlled flight.\n\n4. Programming Skills: Building a self-flying drone requires programming knowledge, particularly in languages like C/C++ for Arduino. Understand the basics of coding, including variables, loops, conditional statements, and functions. Familiarize yourself with libraries and APIs relevant to drone control, such as the Arduino Drone Library or MultiWii.\n\n5. Sensor Integration: Sensors play a crucial role in enabling autonomous flight. Consider integrating sensors like accelerometers, gyroscopes, barometers, and GPS modules. These sensors provide essential data for maintaining stability, altitude control, and navigation.\n\n6. Power Management: Efficient power management is essential for extended flight times. Choose a suitable battery with sufficient capacity and voltage for your drone's requirements. Implement power-saving techniques, such as optimizing code, reducing weight, and using energy-efficient components.\n\n7. Calibration and Testing: Proper calibration of sensors, motors, and flight controllers is crucial for accurate flight control. Follow manufacturer guidelines and perform thorough testing before each flight to ensure stability and reliability.\n\n8. Communication and Control: Establish a reliable communication system between the drone and the ground station. Consider using wireless technologies like Wi-Fi, Bluetooth, or radio frequency modules to transmit data and receive commands.\n\n9. Safety Features: Implement safety features such as fail-safe mechanisms, emergency landing procedures, and obstacle detection systems. These features can prevent accidents and protect your drone from potential damage.\n\n10. Documentation and Troubleshooting: Keep detailed documentation of your build, including wiring diagrams, code explanations, and component specifications. This documentation will be invaluable for troubleshooting and future modifications.\n\nBy considering these important factors, you can embark on your self-flying drone project with confidence. Remember to prioritize safety, thoroughly research and select the right components, acquire programming skills, integrate sensors effectively, manage power efficiently, calibrate and test meticulously, establish reliable communication, implement safety features, and maintain comprehensive documentation. With these considerations in mind, you are well on your way to building a successful self-flying drone using Arduino."]

test_list2 = ['./tmp/797700.png', './tmp/234016.png', './tmp/974939.png', './tmp/410929.png']

def create_pdf(idea, budget, materials):
    class PDF(FPDF):
        def footer(self):
            # Position at 1.5 cm from bottom
            self.set_y(-15)
            # Arial italic 8
            self.set_font('Arial', 'I', 8)
            # Text color in gray
            self.set_text_color(255)

        def title_page(self, idea):
            self.add_page()
            self.set_font('Arial', "I", 32)
            self.set_text_color(0)
            self.cell(0, 50, "DIY Tutorial", 0, 1, 'C', False)
            self.cell(0, 40, "", 0, 1, 'C', False)
            self.cell(0, 110, f"Idea: {idea}", 0, 1, 'C', False)
            self.set_font('Arial', "", 24)
            self.cell(0, 15, '', 0, 1, 'C', False)
            self.cell(0, 20, "", 0, 1, 'C', False)
            self.set_font('Arial', "I", 10)
            self.cell(0, 30, "powered by love at hackthe6ix!", 0, 1, 'C', False)
            self.set_text_color(0, 0, 0)

        def body_page(self, title, output, image):
            self.add_page()
            self.set_font('Arial', "B", 24)
            self.cell(0, 12, title, 0, 1, 'C', False)
            self.set_font('Arial', "", 14)
            fix_unicode = output.replace("’", "'")
            final_output = fix_unicode.replace("•", '- ')
            self.multi_cell(0, 5, final_output.replace("’", "'").replace("“","'").replace("–",'-'))
            self.image(image, x = None, y = None, w = 0, h = 0, type = '', link = '')
   

    pdf = PDF(format="A4")
    pdf.set_title("Ardunio Project - By VisionCraft.ai")
    pdf.title_page(idea)
    pdf.set_font('Arial', "", 24)
    topics = ["Introduction", "Materials", "Procedure", "Considerations"]
    # openai.api_key = "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"
    ai_responses = generate_text(idea, budget, materials)
    # ai_responses = test_list
    ai_images = generate_dalle(f"an Arduino-powered {idea}") 
    ai_images = test_list2
    for index in range(len(ai_responses)):
        pdf.body_page(topics[index], ai_responses[index], ai_images[index])
    """
    # Calls the function
    AI_answers = call_api(company_name, idea, budget)
    for index_number in range(len(topics)):
        try:
            print(AI_answers[index_number])
            # response.json()['choices'][0]['message']['content']
            pdf.body_page(topics[index_number], AI_answers[index_number]['choices'][0]['message']['content'])
        except Exception as err:
            print(f"An Error has occurred! {err}")
            print(AI_answers[index_number])
            pdf.body_page(topics[index_number], f"{err}")
    """
    #pdf.output('server/tmp/business_plan.pdf', 'F')
    #watermark(pdf)
    return pdf

#create_pdf(title="ultrasonic", idea="self flying drone", budget=1000, materials=["arduino", "ultrasonic sensor"])