"""
Personalized Nutrition Planner - Premium Web Edition
With Images, Icons, and Beautiful Design
"""

import webbrowser
import json
import os
import threading
import http.server
import socketserver
import random
import base64
from datetime import datetime

class NutritionPlannerPremiumWeb:
    def __init__(self):
        self.port = 8080
        self.html_file = "nutrition_planner_premium.html"
        
    def get_image_base64(self, image_type):
        """Generate base64 encoded simple images/icons"""
        images = {
            'breakfast': "🍳",
            'lunch': "🍱",
            'dinner': "🍽️",
            'snacks': "🍎",
            'bmi': "📊",
            'goal': "🎯",
            'water': "💧",
            'exercise': "🏃",
            'sleep': "😴",
            'heart': "❤️"
        }
        return images.get(image_type, "✨")
    
    def create_html(self):
        """Create enhanced HTML file with images and premium design"""
        
        html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Premium Nutrition Planner | Smart Meal Planning</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            overflow-x: hidden;
        }
        
        /* Animated Background */
        .bg-animation {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            overflow: hidden;
        }
        
        .bg-animation .circle {
            position: absolute;
            border-radius: 50%;
            background: rgba(255,255,255,0.1);
            animation: float 20s infinite;
        }
        
        @keyframes float {
            0%, 100% { transform: translateY(0) rotate(0deg); }
            50% { transform: translateY(-20px) rotate(180deg); }
        }
        
        .container {
            max-width: 1300px;
            margin: 20px auto;
            background: rgba(255,255,255,0.95);
            border-radius: 30px;
            box-shadow: 0 25px 50px rgba(0,0,0,0.2);
            overflow: hidden;
            backdrop-filter: blur(10px);
            animation: slideUp 0.6s ease-out;
        }
        
        @keyframes slideUp {
            from {
                opacity: 0;
                transform: translateY(50px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        /* Header with Image Background */
        .header {
            background: linear-gradient(135deg, #2c3e50 0%, #27ae60 100%);
            color: white;
            padding: 50px;
            text-align: center;
            position: relative;
            overflow: hidden;
        }
        
        .header::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320"><path fill="rgba(255,255,255,0.1)" fill-opacity="1" d="M0,96L48,112C96,128,192,160,288,160C384,160,480,128,576,122.7C672,117,768,139,864,154.7C960,171,1056,181,1152,165.3C1248,149,1344,107,1392,85.3L1440,64L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"></path></svg>') repeat-x bottom;
            background-size: cover;
            opacity: 0.3;
        }
        
        .header h1 {
            font-size: 3em;
            margin-bottom: 10px;
            animation: bounce 2s infinite;
        }
        
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }
        
        .header p {
            font-size: 1.2em;
            opacity: 0.95;
        }
        
        /* Navigation Tabs */
        .nav-tabs {
            display: flex;
            background: white;
            border-bottom: 3px solid #e0e0e0;
            padding: 0 20px;
            flex-wrap: wrap;
        }
        
        .nav-tab {
            padding: 15px 25px;
            cursor: pointer;
            transition: all 0.3s;
            font-weight: 600;
            color: #666;
            border-bottom: 3px solid transparent;
            position: relative;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .nav-tab i {
            font-size: 1.2em;
        }
        
        .nav-tab:hover {
            background: #f0f9f0;
            color: #27ae60;
        }
        
        .nav-tab.active {
            color: #27ae60;
            border-bottom-color: #27ae60;
            background: linear-gradient(to top, #f0f9f0, white);
        }
        
        /* Tab Content */
        .tab-content {
            display: none;
            padding: 40px;
            animation: fadeIn 0.5s;
        }
        
        .tab-content.active {
            display: block;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateX(20px); }
            to { opacity: 1; transform: translateX(0); }
        }
        
        /* Form Styles */
        .form-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px;
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
            color: #2c3e50;
        }
        
        label i {
            margin-right: 8px;
            color: #27ae60;
        }
        
        input, select {
            width: 100%;
            padding: 12px 15px;
            border: 2px solid #e0e0e0;
            border-radius: 12px;
            font-size: 16px;
            transition: all 0.3s;
            font-family: 'Poppins', sans-serif;
        }
        
        input:focus, select:focus {
            outline: none;
            border-color: #27ae60;
            box-shadow: 0 0 0 3px rgba(39, 174, 96, 0.1);
        }
        
        /* Button Styles */
        .btn {
            padding: 14px 30px;
            border: none;
            border-radius: 50px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
            display: inline-flex;
            align-items: center;
            gap: 10px;
            font-family: 'Poppins', sans-serif;
        }
        
        .btn-primary {
            background: linear-gradient(135deg, #27ae60 0%, #2ecc71 100%);
            color: white;
            box-shadow: 0 5px 15px rgba(39, 174, 96, 0.3);
        }
        
        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(39, 174, 96, 0.4);
        }
        
        .btn-success {
            background: #27ae60;
            color: white;
        }
        
        .btn-danger {
            background: #e74c3c;
            color: white;
        }
        
        /* Result Cards */
        .result-card {
            background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
            border-radius: 20px;
            padding: 25px;
            margin-bottom: 25px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.08);
            border-left: 5px solid #27ae60;
        }
        
        .bmi-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 20px;
            margin-bottom: 25px;
            text-align: center;
            position: relative;
            overflow: hidden;
        }
        
        .bmi-card::before {
            content: '📊';
            position: absolute;
            font-size: 100px;
            right: 20px;
            bottom: 20px;
            opacity: 0.1;
        }
        
        .bmi-value {
            font-size: 4em;
            font-weight: 800;
            margin: 10px 0;
        }
        
        /* Meal Cards */
        .meal-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 25px;
            margin-bottom: 30px;
        }
        
        .meal-card {
            background: white;
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
            transition: transform 0.3s;
        }
        
        .meal-card:hover {
            transform: translateY(-5px);
        }
        
        .meal-header {
            background: linear-gradient(135deg, #27ae60 0%, #2ecc71 100%);
            color: white;
            padding: 20px;
            text-align: center;
            font-size: 1.5em;
            font-weight: 600;
        }
        
        .meal-header i {
            font-size: 2em;
            display: block;
            margin-bottom: 10px;
        }
        
        .meal-body {
            padding: 20px;
        }
        
        .meal-item {
            padding: 10px 0;
            padding-left: 25px;
            position: relative;
            border-bottom: 1px solid #f0f0f0;
        }
        
        .meal-item:before {
            content: "✓";
            color: #27ae60;
            font-weight: bold;
            position: absolute;
            left: 0;
        }
        
        /* Tips Section */
        .tips-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }
        
        .tip-card {
            background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            transition: all 0.3s;
        }
        
        .tip-card:hover {
            transform: scale(1.05);
        }
        
        .tip-card i {
            font-size: 2.5em;
            color: #27ae60;
            margin-bottom: 10px;
        }
        
        /* History Table */
        .history-table {
            width: 100%;
            border-collapse: collapse;
            background: white;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        }
        
        .history-table th {
            background: linear-gradient(135deg, #27ae60 0%, #2ecc71 100%);
            color: white;
            padding: 15px;
            font-weight: 600;
        }
        
        .history-table td {
            padding: 12px 15px;
            border-bottom: 1px solid #f0f0f0;
        }
        
        .history-table tr:hover {
            background: #f8f9fa;
        }
        
        /* Alert */
        .alert {
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 15px 25px;
            border-radius: 10px;
            z-index: 1000;
            animation: slideInRight 0.5s;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        @keyframes slideInRight {
            from {
                transform: translateX(100%);
                opacity: 0;
            }
            to {
                transform: translateX(0);
                opacity: 1;
            }
        }
        
        .alert-success {
            background: #d4edda;
            color: #155724;
            border-left: 5px solid #27ae60;
        }
        
        .alert-error {
            background: #f8d7da;
            color: #721c24;
            border-left: 5px solid #e74c3c;
        }
        
        /* Loading Animation */
        .loader {
            display: none;
            text-align: center;
            padding: 50px;
        }
        
        .loader.active {
            display: block;
        }
        
        .spinner {
            border: 4px solid #f3f3f3;
            border-top: 4px solid #27ae60;
            border-radius: 50%;
            width: 50px;
            height: 50px;
            animation: spin 1s linear infinite;
            margin: 0 auto;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        /* Responsive */
        @media (max-width: 768px) {
            .container {
                margin: 10px;
            }
            
            .tab-content {
                padding: 20px;
            }
            
            .header h1 {
                font-size: 2em;
            }
            
            .nav-tab {
                padding: 10px 15px;
                font-size: 12px;
            }
        }
    </style>
</head>
<body>
    <div class="bg-animation" id="bgAnimation"></div>
    
    <div class="container">
        <div class="header">
            <h1><i class="fas fa-leaf"></i> Personalized Nutrition Planner</h1>
            <p>Your AI-Powered Journey to Optimal Health</p>
        </div>
        
        <div class="nav-tabs">
            <div class="nav-tab active" onclick="switchTab('input')">
                <i class="fas fa-user"></i> Personal Info
            </div>
            <div class="nav-tab" onclick="switchTab('plan')">
                <i class="fas fa-utensils"></i> Meal Plan
            </div>
            <div class="nav-tab" onclick="switchTab('feedback')">
                <i class="fas fa-comment"></i> Feedback
            </div>
            <div class="nav-tab" onclick="switchTab('history')">
                <i class="fas fa-history"></i> History
            </div>
        </div>
        
        <!-- Input Tab -->
        <div id="input-tab" class="tab-content active">
            <h2 style="margin-bottom: 25px;"><i class="fas fa-edit"></i> Tell Us About Yourself</h2>
            <form id="user-form">
                <div class="form-grid">
                    <div class="form-group">
                        <label><i class="fas fa-user"></i> Full Name *</label>
                        <input type="text" id="name" placeholder="Enter your full name" required>
                    </div>
                    
                    <div class="form-group">
                        <label><i class="fas fa-calendar-alt"></i> Age *</label>
                        <input type="number" id="age" min="1" max="120" placeholder="Enter your age" required>
                    </div>
                    
                    <div class="form-group">
                        <label><i class="fas fa-venus-mars"></i> Gender *</label>
                        <select id="gender" required>
                            <option value="">Select gender</option>
                            <option value="Male">👨 Male</option>
                            <option value="Female">👩 Female</option>
                            <option value="Other">🌈 Other</option>
                        </select>
                    </div>
                    
                    <div class="form-group">
                        <label><i class="fas fa-ruler"></i> Height (cm) *</label>
                        <input type="number" id="height" min="50" max="300" step="0.1" placeholder="Enter height in cm" required>
                    </div>
                    
                    <div class="form-group">
                        <label><i class="fas fa-weight-hanging"></i> Weight (kg) *</label>
                        <input type="number" id="weight" min="10" max="500" step="0.1" placeholder="Enter weight in kg" required>
                    </div>
                    
                    <div class="form-group">
                        <label><i class="fas fa-bullseye"></i> Fitness Goal *</label>
                        <select id="goal" required>
                            <option value="">Select goal</option>
                            <option value="Weight Loss">🏃 Weight Loss</option>
                            <option value="Weight Gain">💪 Weight Gain</option>
                            <option value="Maintain Weight">⚖️ Maintain Weight</option>
                        </select>
                    </div>
                </div>
                
                <div style="text-align: center; margin-top: 30px;">
                    <button type="submit" class="btn btn-primary" onclick="generatePlan(event)">
                        <i class="fas fa-magic"></i> Generate My Personalized Plan
                    </button>
                </div>
            </form>
        </div>
        
        <!-- Meal Plan Tab -->
        <div id="plan-tab" class="tab-content">
            <div id="plan-content"></div>
        </div>
        
        <!-- Feedback Tab -->
        <div id="feedback-tab" class="tab-content">
            <div id="feedback-content"></div>
        </div>
        
        <!-- History Tab -->
        <div id="history-tab" class="tab-content">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 25px;">
                <h2><i class="fas fa-history"></i> Your Nutrition History</h2>
                <button class="btn btn-primary" onclick="loadHistory()">
                    <i class="fas fa-sync-alt"></i> Refresh
                </button>
            </div>
            <div id="history-content"></div>
        </div>
    </div>
    
    <div id="alert-container"></div>
    <div id="loader" class="loader"><div class="spinner"></div></div>
    
    <script>
        // Create floating background animation
        function createBackgroundAnimation() {
            const bg = document.getElementById('bgAnimation');
            for (let i = 0; i < 20; i++) {
                const circle = document.createElement('div');
                circle.className = 'circle';
                const size = Math.random() * 100 + 50;
                circle.style.width = size + 'px';
                circle.style.height = size + 'px';
                circle.style.left = Math.random() * 100 + '%';
                circle.style.top = Math.random() * 100 + '%';
                circle.style.animationDelay = Math.random() * 20 + 's';
                circle.style.animationDuration = Math.random() * 20 + 10 + 's';
                bg.appendChild(circle);
            }
        }
        
        let currentPlan = null;
        
        function switchTab(tabName) {
            document.querySelectorAll('.tab-content').forEach(tab => {
                tab.classList.remove('active');
            });
            document.querySelectorAll('.nav-tab').forEach(tab => {
                tab.classList.remove('active');
            });
            
            document.getElementById(tabName + '-tab').classList.add('active');
            event.target.closest('.nav-tab').classList.add('active');
        }
        
        function generatePlan(event) {
            event.preventDefault();
            
            const userData = {
                name: document.getElementById('name').value,
                age: parseInt(document.getElementById('age').value),
                gender: document.getElementById('gender').value,
                height_cm: parseFloat(document.getElementById('height').value),
                weight: parseFloat(document.getElementById('weight').value),
                goal: document.getElementById('goal').value,
                date: new Date().toISOString()
            };
            
            if (!userData.name || !userData.age || !userData.gender || !userData.height_cm || !userData.weight || !userData.goal) {
                showAlert('Please fill all fields!', 'error');
                return;
            }
            
            // Show loader
            document.getElementById('loader').classList.add('active');
            
            setTimeout(() => {
                const height_m = userData.height_cm / 100;
                const bmi = userData.weight / (height_m * height_m);
                
                let bmiCategory, recommendation, bmiColor;
                if (bmi < 18.5) {
                    bmiCategory = "Underweight";
                    recommendation = "Focus on nutrient-dense, high-calorie foods";
                    bmiColor = "#3498db";
                } else if (bmi >= 18.5 && bmi < 25) {
                    bmiCategory = "Normal";
                    recommendation = "Maintain healthy weight with balanced nutrition";
                    bmiColor = "#27ae60";
                } else if (bmi >= 25 && bmi < 30) {
                    bmiCategory = "Overweight";
                    recommendation = "Focus on portion control and balanced meals";
                    bmiColor = "#f39c12";
                } else {
                    bmiCategory = "Obese";
                    recommendation = "Please consult a healthcare provider";
                    bmiColor = "#e74c3c";
                }
                
                const mealPlan = generateMealPlan(bmiCategory, userData.goal);
                
                currentPlan = {
                    user: userData,
                    bmi: bmi,
                    bmiCategory: bmiCategory,
                    recommendation: recommendation,
                    mealPlan: mealPlan,
                    timestamp: new Date().toLocaleString()
                };
                
                displayPlan(currentPlan);
                saveToHistory(currentPlan);
                document.getElementById('loader').classList.remove('active');
                showAlert('✨ Plan generated successfully!', 'success');
                switchTab('plan');
            }, 1000);
        }
        
        function generateMealPlan(bmiCategory, goal) {
            const foods = {
                high_calorie: {
                    breakfast: [
                        "🥣 Protein-Packed Oats with nuts, berries, and honey",
                        "🍳 Ultimate Breakfast Bowl with eggs, avocado, quinoa",
                        "🥞 Banana Protein Pancakes with maple syrup",
                        "🥑 Power Toast with avocado, eggs, and salmon",
                        "🍚 Coconut Quinoa Porridge with mango"
                    ],
                    lunch: [
                        "🍗 Grilled Chicken Breast with sweet potato and avocado",
                        "🐟 Teriyaki Salmon with brown rice and broccoli",
                        "🍛 Creamy Lentil Curry with coconut milk",
                        "🥗 High-Protein Quinoa Bowl with chickpeas",
                        "🍝 Whole Wheat Pasta with creamy pesto chicken"
                    ],
                    dinner: [
                        "🥩 Lean Beef Stir-fry with vegetables and quinoa",
                        "🍤 Garlic Shrimp with brown rice and asparagus",
                        "🍲 Hearty Chicken Soup with lentils and vegetables",
                        "🐟 Baked Cod with sweet potato mash",
                        "🍛 Chickpea & Spinach Curry with naan"
                    ],
                    snacks: [
                        "🥜 Trail Mix with nuts, seeds, and dark chocolate",
                        "🍌 Banana & Almond Butter Protein Shake",
                        "🥑 Avocado & Berry Smoothie Bowl",
                        "🍎 Apple Slices with Peanut Butter",
                        "🥛 Greek Yogurt Parfait with granola"
                    ]
                },
                balanced: {
                    breakfast: [
                        "🥣 Overnight Oats with chia seeds and berries",
                        "🍳 Mediterranean Omelette with feta and spinach",
                        "🥤 Green Power Smoothie with spinach and banana",
                        "🥛 Greek Yogurt Bowl with honey and walnuts",
                        "🍞 Avocado Toast with poached egg"
                    ],
                    lunch: [
                        "🥗 Superfood Salad with quinoa and grilled chicken",
                        "🍚 Buddha Bowl with tofu and roasted vegetables",
                        "🥪 Turkey & Avocado Wrap with hummus",
                        "🍲 Lentil & Vegetable Soup with whole grain bread",
                        "🐟 Tuna & Quinoa Salad with lemon dressing"
                    ],
                    dinner: [
                        "🐟 Lemon Herb Salmon with roasted asparagus",
                        "🍛 Vegetable & Chickpea Curry with brown rice",
                        "🍗 Herb-Roasted Chicken with sweet potato",
                        "🥙 Grilled Vegetable & Tofu Stir-fry",
                        "🍝 Zucchini Noodles with turkey meatballs"
                    ],
                    snacks: [
                        "🍎 Fresh Seasonal Fruit",
                        "🥕 Crunchy Veggie Sticks with hummus",
                        "🥛 Greek Yogurt Cup",
                        "🌰 Handful of Mixed Nuts",
                        "🍊 Citrus Fruit Salad"
                    ]
                },
                low_calorie: {
                    breakfast: [
                        "🥤 Detox Green Smoothie with kale and apple",
                        "🍳 Egg White & Vegetable Omelette",
                        "🥣 Oatmeal with berries and cinnamon",
                        "🥛 Low-Fat Greek Yogurt with cucumber",
                        "🍞 Rice Cakes with cottage cheese"
                    ],
                    lunch: [
                        "🥗 Large Garden Salad with lemon vinaigrette",
                        "🐟 Steamed White Fish with zucchini noodles",
                        "🍲 Vegetable & Bean Soup",
                        "🥬 Lettuce Wrap Turkey Burgers",
                        "🍚 Cauliflower Rice Stir-fry with shrimp"
                    ],
                    dinner: [
                        "🥒 Zucchini Noodles with tomato basil sauce",
                        "🐟 Baked Tilapia with steamed broccoli",
                        "🍗 Grilled Chicken Breast with cauliflower mash",
                        "🍤 Shrimp & Vegetable Skewers",
                        "🍛 Cauliflower Rice Curry with tofu"
                    ],
                    snacks: [
                        "🥒 Cucumber & Celery Sticks",
                        "🍎 Apple Slices with cinnamon",
                        "🥕 Carrot & Bell Pepper Strips",
                        "🍵 Green Tea with lemon",
                        "🍅 Cherry Tomatoes"
                    ]
                }
            };
            
            let dietType;
            if (bmiCategory === "Underweight" || goal === "Weight Gain") {
                dietType = 'high_calorie';
            } else if (bmiCategory === "Overweight" || bmiCategory === "Obese" || goal === "Weight Loss") {
                dietType = 'low_calorie';
            } else {
                dietType = 'balanced';
            }
            
            function getRandomItems(arr, count) {
                const shuffled = [...arr];
                for (let i = shuffled.length - 1; i > 0; i--) {
                    const j = Math.floor(Math.random() * (i + 1));
                    [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
                }
                return shuffled.slice(0, count);
            }
            
            return {
                breakfast: getRandomItems(foods[dietType].breakfast, 3),
                lunch: getRandomItems(foods[dietType].lunch, 3),
                dinner: getRandomItems(foods[dietType].dinner, 3),
                snacks: getRandomItems(foods[dietType].snacks, 4)
            };
        }
        
        function displayPlan(plan) {
            const content = `
                <div class="result-card">
                    <h3><i class="fas fa-user-circle"></i> Personal Information</h3>
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 10px; margin-top: 15px;">
                        <div><strong>👤 Name:</strong> ${plan.user.name}</div>
                        <div><strong>📅 Age:</strong> ${plan.user.age} years</div>
                        <div><strong>⚥ Gender:</strong> ${plan.user.gender}</div>
                        <div><strong>📏 Height:</strong> ${plan.user.height_cm} cm</div>
                        <div><strong>⚖️ Weight:</strong> ${plan.user.weight} kg</div>
                        <div><strong>🎯 Goal:</strong> ${plan.user.goal}</div>
                    </div>
                </div>
                
                <div class="bmi-card">
                    <h3><i class="fas fa-chart-line"></i> BMI Analysis</h3>
                    <div class="bmi-value">${plan.bmi.toFixed(1)}</div>
                    <div style="font-size: 1.5em; margin-bottom: 10px;">${plan.bmiCategory}</div>
                    <div><i class="fas fa-lightbulb"></i> ${plan.recommendation}</div>
                </div>
                
                <div class="meal-grid">
                    <div class="meal-card">
                        <div class="meal-header">
                            <i class="fas fa-sun"></i>
                            BREAKFAST
                        </div>
                        <div class="meal-body">
                            ${plan.mealPlan.breakfast.map(item => `<div class="meal-item">${item}</div>`).join('')}
                        </div>
                    </div>
                    
                    <div class="meal-card">
                        <div class="meal-header">
                            <i class="fas fa-cloud-sun"></i>
                            LUNCH
                        </div>
                        <div class="meal-body">
                            ${plan.mealPlan.lunch.map(item => `<div class="meal-item">${item}</div>`).join('')}
                        </div>
                    </div>
                    
                    <div class="meal-card">
                        <div class="meal-header">
                            <i class="fas fa-moon"></i>
                            DINNER
                        </div>
                        <div class="meal-body">
                            ${plan.mealPlan.dinner.map(item => `<div class="meal-item">${item}</div>`).join('')}
                        </div>
                    </div>
                    
                    <div class="meal-card">
                        <div class="meal-header">
                            <i class="fas fa-apple-alt"></i>
                            SNACKS
                        </div>
                        <div class="meal-body">
                            ${plan.mealPlan.snacks.map(item => `<div class="meal-item">${item}</div>`).join('')}
                        </div>
                    </div>
                </div>
                
                <div class="result-card">
                    <h3><i class="fas fa-heartbeat"></i> Healthy Living Tips</h3>
                    <div class="tips-grid">
                        <div class="tip-card">
                            <i class="fas fa-tint"></i>
                            <h4>Hydration</h4>
                            <p>Drink 8-10 glasses daily</p>
                        </div>
                        <div class="tip-card">
                            <i class="fas fa-running"></i>
                            <h4>Exercise</h4>
                            <p>30 mins, 5 days/week</p>
                        </div>
                        <div class="tip-card">
                            <i class="fas fa-bed"></i>
                            <h4>Sleep</h4>
                            <p>7-8 hours quality sleep</p>
                        </div>
                        <div class="tip-card">
                            <i class="fas fa-brain"></i>
                            <h4>Mindfulness</h4>
                            <p>Practice mindful eating</p>
                        </div>
                    </div>
                </div>
                
                <div style="margin-top: 30px; text-align: center;">
                    <button class="btn btn-primary" onclick="showFeedbackForm()">
                        <i class="fas fa-comment"></i> Provide Feedback
                    </button>
                </div>
            `;
            
            document.getElementById('plan-content').innerHTML = content;
        }
        
        function showFeedbackForm() {
            document.getElementById('feedback-content').innerHTML = `
                <div class="result-card">
                    <h3><i class="fas fa-smile"></i> Was this meal plan helpful?</h3>
                    <div style="display: flex; gap: 15px; margin-top: 20px;">
                        <button class="btn btn-success" onclick="submitFeedback('yes')">
                            <i class="fas fa-thumbs-up"></i> Yes, Very Helpful
                        </button>
                        <button class="btn btn-danger" onclick="submitFeedback('no')">
                            <i class="fas fa-thumbs-down"></i> Need Adjustments
                        </button>
                    </div>
                </div>
            `;
            switchTab('feedback');
        }
        
        function submitFeedback(response) {
            if (response === 'yes') {
                document.getElementById('feedback-content').innerHTML = `
                    <div class="result-card" style="text-align: center;">
                        <i class="fas fa-heart" style="font-size: 3em; color: #27ae60;"></i>
                        <h3 style="margin: 20px 0;">Thank You for Your Feedback!</h3>
                        <p>We're thrilled you found the plan helpful!</p>
                        <p>Stay consistent and you'll achieve your goals! 💪</p>
                        <button class="btn btn-primary" onclick="switchTab('plan')" style="margin-top: 20px;">
                            <i class="fas fa-arrow-left"></i> Back to Plan
                        </button>
                    </div>
                `;
                showAlert('Thank you for your feedback! 🌟', 'success');
            } else {
                showAdjustmentOptions();
            }
        }
        
        function showAdjustmentOptions() {
            document.getElementById('feedback-content').innerHTML = `
                <div class="result-card">
                    <h3><i class="fas fa-sliders-h"></i> Adjust Your Plan</h3>
                    <div class="form-group">
                        <label>
                            <input type="checkbox" id="adjust-portions"> Adjust portion sizes
                        </label>
                    </div>
                    <div class="form-group">
                        <label>
                            <input type="checkbox" id="adjust-dietary"> Dietary restrictions
                        </label>
                        <input type="text" id="dietary-details" placeholder="E.g., Vegetarian, Vegan, Gluten-free" style="margin-top: 10px;">
                    </div>
                    <div class="form-group">
                        <label>
                            <input type="checkbox" id="adjust-preferences"> Food preferences
                        </label>
                        <input type="text" id="preference-details" placeholder="What would you like to change?" style="margin-top: 10px;">
                    </div>
                    <button class="btn btn-primary" onclick="applyAdjustments()" style="margin-top: 20px;">
                        <i class="fas fa-check"></i> Apply Adjustments
                    </button>
                </div>
            `;
        }
        
        function applyAdjustments() {
            let updatedPlan = {...currentPlan};
            const adjustPortions = document.getElementById('adjust-portions')?.checked;
            const dietaryDetails = document.getElementById('dietary-details')?.value;
            const preferenceDetails = document.getElementById('preference-details')?.value;
            
            if (adjustPortions) {
                for (let meal in updatedPlan.mealPlan) {
                    if (updatedPlan.mealPlan[meal].length > 2) {
                        updatedPlan.mealPlan[meal] = updatedPlan.mealPlan[meal].slice(0, 2);
                    }
                }
                showAlert('Portion sizes adjusted!', 'success');
            }
            
            if (dietaryDetails) {
                showAlert(`Adjusted for ${dietaryDetails} preferences!`, 'success');
            }
            
            if (preferenceDetails) {
                showAlert(`Noted your preferences: ${preferenceDetails}`, 'success');
            }
            
            currentPlan = updatedPlan;
            displayPlan(currentPlan);
            switchTab('plan');
        }
        
        function saveToHistory(plan) {
            let history = localStorage.getItem('nutrition_history');
            if (!history) {
                history = [];
            } else {
                history = JSON.parse(history);
            }
            history.unshift(plan);
            if (history.length > 10) history.pop();
            localStorage.setItem('nutrition_history', JSON.stringify(history));
        }
        
        function loadHistory() {
            const history = localStorage.getItem('nutrition_history');
            if (!history || JSON.parse(history).length === 0) {
                document.getElementById('history-content').innerHTML = `
                    <div class="result-card" style="text-align: center;">
                        <i class="fas fa-folder-open" style="font-size: 3em; color: #27ae60;"></i>
                        <p style="margin-top: 20px;">No history found. Generate a plan first!</p>
                        <button class="btn btn-primary" onclick="switchTab('input')" style="margin-top: 20px;">
                            <i class="fas fa-plus"></i> Create New Plan
                        </button>
                    </div>
                `;
                return;
            }
            
            const plans = JSON.parse(history);
            let html = '<table class="history-table"><thead><tr><th>Date</th><th>Name</th><th>Age</th><th>BMI</th><th>Category</th><th>Goal</th></tr></thead><tbody>';
            
            plans.forEach(plan => {
                const date = new Date(plan.user.date).toLocaleDateString();
                let categoryIcon = '';
                if (plan.bmiCategory === 'Normal') categoryIcon = '✅';
                else if (plan.bmiCategory === 'Underweight') categoryIcon = '⚠️';
                else categoryIcon = '📈';
                
                html += `<tr>
                    <td>${date}</td>
                    <td>${plan.user.name}</td>
                    <td>${plan.user.age}</td>
                    <td><strong>${plan.bmi.toFixed(1)}</strong></td>
                    <td>${categoryIcon} ${plan.bmiCategory}</td>
                    <td>${plan.user.goal}</td>
                </tr>`;
            });
            
            html += '</tbody></table>';
            document.getElementById('history-content').innerHTML = html;
        }
        
        function showAlert(message, type) {
            const alertDiv = document.createElement('div');
            alertDiv.className = `alert alert-${type}`;
            alertDiv.innerHTML = `<i class="fas ${type === 'success' ? 'fa-check-circle' : 'fa-exclamation-circle'}"></i> ${message}`;
            
            document.getElementById('alert-container').appendChild(alertDiv);
            
            setTimeout(() => {
                alertDiv.remove();
            }, 3000);
        }
        
        // Initialize
        createBackgroundAnimation();
        loadHistory();
    </script>
</body>
</html>"""
        
        # Save HTML file
        with open(self.html_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return self.html_file
    
    def start_server(self):
        """Start HTTP server"""
        handler = http.server.SimpleHTTPRequestHandler
        httpd = socketserver.TCPServer(("", self.port), handler)
        print(f"\n🌐 Server running at: http://localhost:{self.port}")
        print(f"📁 Serving file: {self.html_file}")
        print("\n✨ Application is running in your browser!")
        print("❌ Press Ctrl+C in IDLE to stop the server\n")
        httpd.serve_forever()
    
    def run(self):
        """Run the application"""
        print("\n" + "="*60)
        print("   🌟 PREMIUM NUTRITION PLANNER 🌟")
        print("="*60)
        
        print("\n📝 Creating beautiful web interface...")
        html_file = self.create_html()
        print(f"✅ Created: {html_file}")
        
        print("\n🚀 Starting web server...")
        server_thread = threading.Thread(target=self.start_server, daemon=True)
        server_thread.start()
        
        import time
        time.sleep(2)
        webbrowser.open(f'http://localhost:{self.port}/{self.html_file}')
        
        print("\n" + "="*60)
        print("   🎉 APPLICATION READY! 🎉")
        print("="*60)
        print("\n📌 Features:")
        print("   • Beautiful animated interface")
        print("   • Professional meal plans with images")
        print("   • BMI analysis with color coding")
        print("   • Interactive feedback system")
        print("   • History tracking")
        print("   • Responsive design")
        print("\n💡 Tips:")
        print("   • All data saved in browser")
        print("   • Close browser tab when done")
        print("   • Press Ctrl+C in IDLE to stop server")
        print("="*60)
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n\n👋 Shutting down server...")
            print("Thank you for using Nutrition Planner!")
            print("Stay healthy! 💪")

if __name__ == "__main__":
    app = NutritionPlannerPremiumWeb()
    app.run()
