#CS50 Jobroom

##Video Demo: https://www.youtube.com/watch?v=HLcEIMK2ER0

###Description:

    Hello World!

    Welcome to CS50 Jobroom, a comprehensive web application designed to revolutionize the job market experience. My name is Marek, and I'm thrilled to present my final project for CS50.

    CS50 Jobroom aims to bridge the gap between job seekers and employers by providing a user-friendly platform to post and search for job opportunities.
    By leveraging the power of technology and the skills I've acquired throughout the course, I've developed a dynamic web application that simplifies the job search process.

    To bring CS50 Jobroom to life, I utilized a combination of technologies, including Flask, a powerful Python web framework, along with CSS, JavaScript, and HTML. These technologies enabled me to create an intuitive and visually appealing interface that enhances user experience.

    At the heart of CS50 Jobroom is the main program, app.py, which serves as the backbone of the application. It handles various functionalities such as user authentication, database management, and routing. In addition to app.py, I incorporated additional resources to enhance the website's aesthetics and functionality. The "static" directory contains CSS stylesheets, graphics, and helper functions that contribute to the overall user experience.

    CS50 Jobroom consists of eight distinct pages, each designed to serve a specific purpose. Let's explore each of these pages in detail:

    add.html: This page allows users to contribute to the job market by adding new job listings. It features user-friendly input fields where users can provide essential details such as company name, position title, location, and contact information. Once submitted, the job details are securely stored in the JOBS database, ensuring that potential candidates can discover and apply for the posted opportunities.

    error.html: As with any web application, it's essential to handle errors gracefully. The error.html page comes into play when users encounter issues such as entering incorrect login credentials or encountering technical errors. This page displays informative error messages with cute memes, guiding users on how to rectify the situation and proceed smoothly with their tasks.

    home.html: The home page serves as a warm and inviting introduction to CS50 Jobroom. It provides a brief overview of the website's functionalities and offers step-by-step instructions on how to navigate and make the most of the platform. This page sets the tone for a user-friendly and inclusive job market experience.

    jobs.html: This section of CS50 Jobroom is dedicated to showcasing all available job opportunities. By tapping into the JOBS database, the website dynamically retrieves and displays a comprehensive list of jobs posted by various users. In this interface, users can explore job details, company information, location and date when job was listed. This page acts as a centralized hub for job seekers to discover and pursue their desired career.

    layout.html: Providing consistency across the website's design and layout, layout.html serves as the primary template for all pages within CS50 Jobroom. It establishes a cohesive visual identity, ensuring that users have a seamless experience while navigating between different sections of the website. From the header and navigation bar to the footer, layout.html harmonizes the overall aesthetic and enhances user engagement.

    login.html: User authentication is a fundamental aspect of CS50 Jobroom. The login.html page enables registered users to securely access their accounts. By entering their credentials, users can verify their identity and gain personalized access to their profile, previously posted jobs, and other account-specific features. The login process involves authentication checks against the USERS database to ensure the security and privacy of user data.

    posted.html: When users log into their CS50 Jobroom accounts, they can access the posted.html page to manage their job listings. This page displays the jobs posted by the currently logged-in user, providing a clear overview of their active postings. After finding a great applicant users are allowed here to delete their posted jobs.

    register.html: To expand the CS50 Jobroom community, register.html offers a simple and intuitive registration process for new users. This page presents a registration form where individuals can create a new account by providing their personal information and setting up their login credentials. Register.html also handles various error scenarios, ensuring that the registration process remains smooth and error-free.

    The USERS database is a crucial component of CS50 Jobroom, housing user-related information such as usernames, passwords(hashed), and additional profile details. The JOBS database, on the other hand, stores the specific details of the jobs posted on the website, facilitating seamless job discovery and application processes.

    In summary, CS50 Jobroom represents the culmination of my CS50 journey. It combines my passion for programming, my appreciation for user-centric design, and my desire to facilitate meaningful connections in the job market.

    Thank you for taking the time to explore CS50 Jobroom. I hope this overview provides insight into the project's features and the effort invested in its development.