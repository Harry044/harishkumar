import React from 'react';

const Skills = () => {
  const skillsData = [
    {
      category: "Data & Analytics Tools",
      skills: ["Power BI Desktop", "MySQL", "Advanced Excel", "Data Visualization", "Statistical Analysis"],
      icon: "📊",
      color: "bg-deep-blue",
      textColor: "text-deep-blue"
    },
    {
      category: "Programming Languages",
      skills: ["Python", "C++ Object Oriented Programming", "SQL", "Arduino IDE"],
      icon: "💻",
      color: "bg-olive-green",
      textColor: "text-olive-green"
    },
    {
      category: "Core Competencies", 
      skills: ["Machine Learning", "Data Science", "Economic Analysis", "Research Methods", "Project Management"],
      icon: "🧠",
      color: "bg-digital-crimson",
      textColor: "text-digital-crimson"
    }
  ];

  const backgroundImage = "https://images.unsplash.com/photo-1666875753105-c63a6f3bdc86?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2NzZ8MHwxfHNlYXJjaHwxfHxhbmFseXRpY3N8ZW58MHx8fHwxNzUzNzg4NDQ5fDA&ixlib=rb-4.1.0&q=85";

  return (
    <section id="skills" className="py-20 bg-gradient-to-br from-deep-blue to-light-blue relative">
      {/* Background overlay */}
      <div 
        className="absolute inset-0 opacity-10"
        style={{
          backgroundImage: `url(${backgroundImage})`,
          backgroundSize: 'cover',
          backgroundPosition: 'center'
        }}
      ></div>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        {/* Section Header */}
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold text-white mb-4">
            My <span className="text-olive-green">Skills</span>
          </h2>
          <div className="w-24 h-1 bg-olive-green mx-auto mb-8"></div>
          <p className="text-lg text-blue-100 max-w-3xl mx-auto">
            Currently learning cutting-edge technologies in Data Science, AI, and Analytics
          </p>
        </div>

        {/* Skills Grid */}
        <div className="grid md:grid-cols-3 gap-8">
          {skillsData.map((category, index) => (
            <div
              key={index}
              className="bg-white rounded-2xl shadow-xl p-8 card-hover animate-slide-up"
              style={{animationDelay: `${index * 0.2}s`}}
            >
              {/* Category Header */}
              <div className="text-center mb-8">
                <div className="text-6xl mb-4">{category.icon}</div>
                <h3 className={`text-2xl font-bold ${category.textColor} mb-2`}>
                  {category.category}
                </h3>
                <div className={`w-16 h-1 ${category.color} mx-auto rounded-full`}></div>
              </div>

              {/* Skills List */}
              <div className="space-y-4">
                {category.skills.map((skill, skillIndex) => (
                  <div
                    key={skillIndex}
                    className="flex items-center space-x-3 p-3 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors duration-300"
                  >
                    <div className={`w-3 h-3 ${category.color} rounded-full flex-shrink-0`}></div>
                    <span className="text-gray-700 font-medium">{skill}</span>
                  </div>
                ))}
              </div>

              {/* Learning Status */}
              <div className="mt-8 pt-6 border-t border-gray-200">
                <div className="flex justify-between items-center mb-2">
                  <span className="text-sm font-medium text-gray-600">Learning Status</span>
                  <span className="text-sm font-medium text-gray-800">
                    {index === 0 ? "Intermediate" : index === 1 ? "Learning" : "Advanced"}
                  </span>
                </div>
                <div className="w-full bg-gray-200 rounded-full h-2">
                  <div
                    className={`h-2 rounded-full ${category.color} transition-all duration-1000 ease-out`}
                    style={{
                      width: index === 0 ? "75%" : index === 1 ? "60%" : "85%"
                    }}
                  ></div>
                </div>
              </div>
            </div>
          ))}
        </div>

        {/* Learning Journey Section */}
        <div className="mt-16 bg-white/10 backdrop-blur-sm rounded-2xl p-8">
          <h3 className="text-2xl font-bold text-white text-center mb-8">
            🚀 Currently Learning
          </h3>
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            {[
              { name: "Machine Learning", progress: "60%", icon: "🤖" },
              { name: "Python Programming", progress: "70%", icon: "🐍" },
              { name: "Power BI", progress: "65%", icon: "📊" },
              { name: "SQL Database", progress: "75%", icon: "🗃️" }
            ].map((skill, index) => (
              <div
                key={index}
                className="text-center p-4 bg-white/20 rounded-xl hover:bg-white/30 transition-all duration-300"
              >
                <div className="text-3xl mb-2">{skill.icon}</div>
                <h4 className="text-white font-semibold mb-2">{skill.name}</h4>
                <div className="w-full bg-white/30 rounded-full h-2 mb-1">
                  <div 
                    className="h-2 rounded-full bg-olive-green transition-all duration-1000 ease-out"
                    style={{width: skill.progress}}
                  ></div>
                </div>
                <span className="text-olive-green text-sm font-medium">{skill.progress}</span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
};

export default Skills;