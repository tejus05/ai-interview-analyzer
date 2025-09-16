"""
Sample interview transcripts for testing the bias detection system
Contains various scenarios including both biased and unbiased interviews
"""

SAMPLE_INTERVIEWS = {
    "Fair Technical Interview": """
Interviewer: Good morning! Thank you for coming in today. Let's start by having you tell me about your experience with Python and data structures.

Candidate: Good morning! I've been working with Python for about 3 years now. I'm particularly experienced with lists, dictionaries, and sets. In my recent project, I implemented a hash table-based caching system that improved our application's response time by 40%.

Interviewer: That's impressive. Can you walk me through how you would approach designing a system to handle user authentication?

Candidate: Sure. I'd start by considering the security requirements - we'd need secure password hashing, probably using bcrypt or similar. For scalability, I'd implement JWT tokens for session management. The database would store user credentials securely, and we'd need rate limiting to prevent brute force attacks.

Interviewer: Great approach. Now, let's do a coding exercise. How would you find the second largest number in an array?

Candidate: I'd iterate through the array once, keeping track of the largest and second largest values. Here's my approach... [explains algorithm step by step]

Interviewer: Excellent problem-solving skills. Do you have any questions about the role or our engineering culture?

Candidate: Yes, I'm curious about the team structure and how you handle code reviews and technical mentorship.

Interviewer: We have a collaborative culture with peer code reviews and regular tech talks. We believe in continuous learning and knowledge sharing.
    """,
    
    "Biased Interview - Gender": """
Interviewer: Hi there! So you're Sarah, right? I have to ask - this is a pretty demanding role with long hours. Are you planning to have kids anytime soon? We need someone who can really commit to the position.

Candidate: I'm here to discuss my qualifications for the software engineer position. I have 5 years of experience in full-stack development.

Interviewer: Right, right. But you know how it is with women in tech - they often leave when they start families. Are you married? Your husband okay with you working late nights?

Candidate: My personal life doesn't affect my professional capabilities. I've consistently delivered projects on time and have experience with React, Node.js, and cloud platforms.

Interviewer: Sure, but I'm just being practical here. We had another girl who left after getting pregnant. Cost us a lot in training. So what's your plan there?

Candidate: I'd prefer to focus on the technical requirements. Would you like to see my portfolio?

Interviewer: Yeah, okay. But just so you know, this team is mostly guys - very technical, lots of sports talk. You think you'd fit in with that kind of atmosphere?

Candidate: I'm confident in my technical abilities and collaboration skills regardless of team composition.

Interviewer: Alright, well, let's see... Do you think you can handle the pressure? Sometimes the guys get pretty intense during crunch time.
    """,
    
    "Biased Interview - Age": """
Interviewer: So, John, I see you've been in the industry for quite a while. Born in 1965, so that makes you... 58? That's getting up there for a software developer.

Candidate: I have over 30 years of experience in software development, with recent expertise in modern frameworks like React and cloud technologies.

Interviewer: Yeah, but don't you think this might be a young person's game? All this new technology, agile methodologies... Our team is mostly millennials. They work fast, adapt quickly to new tech stacks.

Candidate: I've consistently adapted to new technologies throughout my career. I recently completed certifications in AWS and have been working with Docker and Kubernetes.

Interviewer: But honestly, how do you keep up? I mean, at your age, learning new programming languages must be tough. Our codebase uses the latest JavaScript features, microservices...

Candidate: I've been working with microservices architecture for the past 3 years and I'm very comfortable with ES6+ JavaScript features.

Interviewer: Right, but the energy level... Can you handle the startup pace? Late nights, weekend deployments? The young guys don't seem to mind, but...

Candidate: I've managed critical deployments and high-pressure situations throughout my career. My experience actually helps me work more efficiently.

Interviewer: I'm just concerned about cultural fit. The team likes to go out for drinks, play video games during breaks. You might feel out of place with all these twenty-somethings.
    """,
    
    "Biased Interview - Education": """
Interviewer: I see here you went to State University. Interesting. Most of our team is from MIT, Stanford, you know, the top-tier schools. Tell me about that choice.

Candidate: I chose State University because of their strong computer science program and research opportunities. I graduated summa cum laude and worked on several open-source projects.

Interviewer: Right, but we're used to a certain caliber here. Our algorithms are pretty sophisticated - not sure if State University prepared you for that level of complexity.

Candidate: I've worked on complex distributed systems and have contributed to open-source projects with thousands of stars on GitHub. My portfolio demonstrates my problem-solving abilities.

Interviewer: Sure, but there's something about the Ivy League network, you know? These guys just think differently. They've been around excellence their whole lives.

Candidate: I believe my work speaks for itself. I've increased system performance by 60% in my current role and led a team of 5 developers.

Interviewer: Look, I'm not saying you're not smart, but culturally... Our clients expect a certain pedigree. When they see MIT or Stanford on the resume, they just have more confidence.

Candidate: I understand the importance of client confidence, but I believe delivering quality work is what builds trust long-term.

Interviewer: Maybe, but honestly, I'm wondering if you'll be able to keep up with our PhD-level discussions. The team talks about complex theoretical concepts during lunch.

Candidate: I've published papers on machine learning algorithms and regularly engage with academic research to stay current.
    """,
    
    "Biased Interview - Multiple Issues": """
Interviewer: So, Maria, interesting name. Where are you originally from? Your accent is pretty thick.

Candidate: I'm from California, born and raised. I'd like to discuss my qualifications for the senior developer position.

Interviewer: California, huh? But your family, where are they from originally? You look Hispanic. We don't have many of those in our engineering team.

Candidate: I have 7 years of experience in full-stack development and have led multiple successful projects.

Interviewer: Right, right. But I have to ask - you're what, like 35? And unmarried? That's unusual for a Latina woman, isn't it? Family pressure and all that?

Candidate: My personal life is private. I'd prefer to focus on my technical skills and experience.

Interviewer: Sure, but I'm just trying to understand if you're going to be stable here. Hispanic families are very traditional, lots of kids, you know? Plus at your age, the biological clock and all...

Candidate: I've been consistently promoted in my previous roles and have excellent performance reviews.

Interviewer: Okay, but honestly, our team is very... how do I put this... intellectual. Lots of advanced degrees, people who went to good schools. You went to a community college first, right? Different background.

Candidate: I transferred to UC Berkeley and graduated with honors in Computer Science.

Interviewer: Berkeley, sure, but starting at community college... Look, I'm not being racist or anything, but our clients are mostly white professionals. They expect to work with people who... well, you know, people they can relate to.

Candidate: I believe my work quality and professional communication skills are what matter most to clients.
    """,
    
    "Professional Unbiased Interview": """
Interviewer: Good afternoon! I'm excited to learn about your background and experience. Could you start by telling me about your most challenging project?

Candidate: Good afternoon! In my previous role, I led the development of a real-time analytics platform that processed over 1 million events per second. The main challenge was ensuring data consistency while maintaining low latency.

Interviewer: That sounds complex. How did you approach the architecture design?

Candidate: We used an event-driven architecture with Apache Kafka for message streaming and Redis for caching. I had to balance performance requirements with data reliability, so we implemented eventual consistency patterns.

Interviewer: Interesting solution. What programming languages and frameworks did you use?

Candidate: The backend was primarily Java with Spring Boot, and we used React for the frontend dashboard. We also incorporated Python for some data processing tasks and used Docker for containerization.

Interviewer: Great technology stack. How do you stay current with new technologies and best practices?

Candidate: I regularly attend tech meetups, contribute to open-source projects, and take online courses. I also follow industry blogs and participate in code reviews to learn from colleagues.

Interviewer: That's excellent. Our team values continuous learning. Can you describe a time when you had to collaborate with non-technical stakeholders?

Candidate: I worked closely with the product and marketing teams to define requirements for a customer-facing dashboard. I had to translate technical constraints into business impact and find solutions that worked for everyone.

Interviewer: Perfect. Do you have any questions about our engineering practices or company culture?

Candidate: Yes, I'm curious about your approach to code quality, testing practices, and how you handle technical debt.

Interviewer: We emphasize test-driven development, have automated CI/CD pipelines, and dedicate 20% of each sprint to addressing technical debt. We believe in sustainable development practices.
    """
}

# Metadata about each interview for additional context
INTERVIEW_METADATA = {
    "Fair Technical Interview": {
        "bias_level": "None",
        "focus": "Technical skills and problem-solving",
        "expected_biases": []
    },
    "Biased Interview - Gender": {
        "bias_level": "High",
        "focus": "Gender-based assumptions and stereotypes",
        "expected_biases": ["Gender", "Personal Life", "Stereotyping"]
    },
    "Biased Interview - Age": {
        "bias_level": "High", 
        "focus": "Age discrimination and stereotypes",
        "expected_biases": ["Age", "Stereotyping", "Cultural Fit"]
    },
    "Biased Interview - Education": {
        "bias_level": "Medium",
        "focus": "Educational elitism and class bias",
        "expected_biases": ["Education Background", "Socioeconomic Status", "Elitism"]
    },
    "Biased Interview - Multiple Issues": {
        "bias_level": "Severe",
        "focus": "Multiple intersecting biases",
        "expected_biases": ["Race/Ethnicity", "Gender", "Age", "Education Background", "Appearance"]
    },
    "Professional Unbiased Interview": {
        "bias_level": "None",
        "focus": "Skills-based professional assessment",
        "expected_biases": []
    }
}