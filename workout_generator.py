import tkinter as tk
import random
from tkinter import messagebox

root = tk.Tk()
root.title("Custom Workout Generator")
root.geometry("1000x600")  

root.configure(bg="#B6CDD9")

canvas = tk.Canvas(root, bg="#B6CDD9", highlightthickness=0)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

scrollable_frame = tk.Frame(canvas, bg="#B6CDD9")
canvas_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="n")

def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

scrollable_frame.bind("<Configure>", on_frame_configure)


def center_frame(event):
    canvas.itemconfig(canvas_window, width=event.width)

canvas.bind("<Configure>", center_frame)

heading = tk.Label(scrollable_frame, text="Your Customised Workout Generator!", 
                   font=("Arial", 16, "bold"),fg="#F7F7F8", bg="#0B3760",  pady=2)
heading.pack_configure()

gender_label = tk.Label(scrollable_frame,
                        text="1) Select your gender",
                        font=("Arial", 14, "bold"),
                        fg="#0B3760",
                        bg="#B6CDD9",
                        pady=25)
gender_label.pack()

gender_frame = tk.Frame(scrollable_frame, bg="#B6CDD9")
gender_frame.pack(pady=15)

gender_var = tk.StringVar(value="Male")  

male_radio = tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male",
                            font=("Arial", 12), fg="#0B3760", bg="#B6CDD9",
                            selectcolor="#B6CDD9", activebackground="#B6CDD9")
male_radio.pack(side="left", padx=20) 

female_radio = tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female",
                              font=("Arial", 12), fg="#0B3760", bg="#B6CDD9",
                              selectcolor="#B6CDD9", activebackground="#B6CDD9")
female_radio.pack(side="left", padx=20)  

age_label = tk.Label(scrollable_frame,
                     text="2) Enter your age:",
                     font=("Arial", 14, "bold"),
                     fg="#0B3760",
                     bg="#B6CDD9",
                     pady=2)
age_label.pack()

age_var = tk.StringVar()
age_entry = tk.Entry(scrollable_frame, textvariable=age_var, font=("Arial", 12),width=8)
age_entry.pack(pady=25)

goals_label = tk.Label(scrollable_frame,
                     text="3) What are your fitness goals?",
                     font=("Arial", 14, "bold"),
                     fg="#0B3760",
                     bg="#B6CDD9",
                     pady=2)
goals_label.pack()


goal_frame = tk.Frame(scrollable_frame, bg="#B6CDD9")
goal_frame.pack(pady=25)

lose_weight_var = tk.IntVar()
gain_strength_var = tk.IntVar()
gain_muscle_var = tk.IntVar()
improve_endurance_var = tk.IntVar()
improve_flexibility_var = tk.IntVar()
boost_fitness_var = tk.IntVar()

tk.Checkbutton(goal_frame, text="Lose Weight", variable=lose_weight_var,
               font=("Arial", 12), fg="#0B3760", bg="#B6CDD9", selectcolor="#B6CDD9")\
               .grid(row=0, column=0, padx=10, pady=5, sticky="w")
tk.Checkbutton(goal_frame, text="Gain Strength", variable=gain_strength_var,
               font=("Arial", 12), fg="#0B3760", bg="#B6CDD9", selectcolor="#B6CDD9")\
               .grid(row=0, column=1, padx=10, pady=5, sticky="w")
tk.Checkbutton(goal_frame, text="Gain Muscle", variable=gain_muscle_var,
               font=("Arial", 12), fg="#0B3760", bg="#B6CDD9", selectcolor="#B6CDD9")\
               .grid(row=0, column=2, padx=10, pady=5, sticky="w")

tk.Checkbutton(goal_frame, text="Improve Endurance", variable=improve_endurance_var,
               font=("Arial", 12), fg="#0B3760", bg="#B6CDD9", selectcolor="#B6CDD9")\
               .grid(row=1, column=0, padx=10, pady=5, sticky="w")
tk.Checkbutton(goal_frame, text="Increase Flexibility", variable=improve_flexibility_var,
               font=("Arial", 12), fg="#0B3760", bg="#B6CDD9", selectcolor="#B6CDD9")\
               .grid(row=1, column=1, padx=10, pady=5, sticky="w")
tk.Checkbutton(goal_frame, text="Boost Overall Fitness", variable=boost_fitness_var,
               font=("Arial", 12), fg="#0B3760", bg="#B6CDD9", selectcolor="#B6CDD9")\
               .grid(row=1, column=2, padx=10, pady=5, sticky="w")

level_label = tk.Label(scrollable_frame,
                        text="4) Select your fitness level",
                        font=("Arial", 14, "bold"),
                        fg="#0B3760",
                        bg="#B6CDD9",
                        pady=2)
level_label.pack()

level_frame = tk.Frame(scrollable_frame, bg="#B6CDD9")
level_frame.pack(pady=25)

level_var = tk.StringVar(value="Male")  

beginner_radio = tk.Radiobutton(level_frame, text="Beginner", variable=level_var, value="Beginner",
                            font=("Arial", 12), fg="#0B3760", bg="#B6CDD9",
                            selectcolor="#B6CDD9", activebackground="#B6CDD9")
beginner_radio.pack(side="left", padx=20) 

intermidiate_radio = tk.Radiobutton(level_frame, text="Intermidiate", variable=level_var, value="Intermidiate",
                            font=("Arial", 12), fg="#0B3760", bg="#B6CDD9",
                            selectcolor="#B6CDD9", activebackground="#B6CDD9")
intermidiate_radio.pack(side="left", padx=20) 

advanced_radio = tk.Radiobutton(level_frame, text="Advanced", variable=level_var, value="Advanced",
                            font=("Arial", 12), fg="#0B3760", bg="#B6CDD9",
                            selectcolor="#B6CDD9", activebackground="#B6CDD9")
advanced_radio.pack(side="left", padx=20) 


equipment_label = tk.Label(scrollable_frame,
                     text="5) Select your preferred equipment",
                     font=("Arial", 14, "bold"),
                     fg="#0B3760",
                     bg="#B6CDD9",
                     pady=2)
equipment_label.pack()

equipment_frame = tk.Frame(scrollable_frame, bg="#B6CDD9")
equipment_frame.pack(pady=25)

barbell_var = tk.IntVar()
dumbbells_var = tk.IntVar()
bodyweight_var = tk.IntVar()
machine_var = tk.IntVar()
kettlebells_var = tk.IntVar()
cables_var = tk.IntVar()
band_var = tk. IntVar()

tk.Checkbutton(equipment_frame, text="Barbell", variable=barbell_var,
               font=("Arial", 12), fg="#0B3760", bg="#B6CDD9", selectcolor="#B6CDD9")\
               .grid(row=0, column=0, padx=10, pady=5, sticky="w")
tk.Checkbutton(equipment_frame, text="Dumbbells", variable=dumbbells_var,
               font=("Arial", 12), fg="#0B3760", bg="#B6CDD9", selectcolor="#B6CDD9")\
               .grid(row=0, column=1, padx=10, pady=5, sticky="w")
tk.Checkbutton(equipment_frame, text="Body Weight", variable=bodyweight_var,
               font=("Arial", 12), fg="#0B3760", bg="#B6CDD9", selectcolor="#B6CDD9")\
               .grid(row=0, column=2, padx=10, pady=5, sticky="w")

tk.Checkbutton(equipment_frame, text="Machine", variable=machine_var,
               font=("Arial", 12), fg="#0B3760", bg="#B6CDD9", selectcolor="#B6CDD9")\
               .grid(row=1, column=0, padx=10, pady=5, sticky="w")
tk.Checkbutton(equipment_frame, text="Kettlebells", variable=kettlebells_var,
               font=("Arial", 12), fg="#0B3760", bg="#B6CDD9", selectcolor="#B6CDD9")\
               .grid(row=1, column=1, padx=10, pady=5, sticky="w")
tk.Checkbutton(equipment_frame, text="Cables", variable=cables_var,
               font=("Arial", 12), fg="#0B3760", bg="#B6CDD9", selectcolor="#B6CDD9")\
               .grid(row=1, column=2, padx=10, pady=5, sticky="w")
tk.Checkbutton(equipment_frame, text="Band", variable=band_var,
               font=("Arial", 12), fg="#0B3760", bg="#B6CDD9", selectcolor="#B6CDD9")\
               .grid(row=2, column=0, padx=10, pady=5, sticky="w")

muscle_label = tk.Label(scrollable_frame,
                     text="6) What would you like to train?",
                     font=("Arial", 14, "bold"),
                     fg="#0B3760",
                     bg="#B6CDD9",
                     pady=2)
muscle_label.pack()

muscle_frame = tk.Frame(scrollable_frame, bg="#B6CDD9")
muscle_frame.pack(pady=25)

chest_var = tk.IntVar()
back_var = tk.IntVar()
legs_var = tk.IntVar()
arms_var = tk.IntVar()
core_var = tk.IntVar()

tk.Checkbutton(muscle_frame, text="Chest (Pectorals)", variable=chest_var,
               font=("Arial", 12), fg="#0B3760", bg="#B6CDD9", selectcolor="#B6CDD9")\
               .grid(row=0, column=0, padx=10, pady=5, sticky="w")
tk.Checkbutton(muscle_frame, text="Back (Latissimus Dorsi & Trapezius)", variable=back_var,
               font=("Arial", 12), fg="#0B3760", bg="#B6CDD9", selectcolor="#B6CDD9")\
               .grid(row=0, column=1, padx=10, pady=5, sticky="w")
tk.Checkbutton(muscle_frame, text="Legs (Quadriceps, Hamstrings, Glutes, Calves)", variable=legs_var,
               font=("Arial", 12), fg="#0B3760", bg="#B6CDD9", selectcolor="#B6CDD9")\
               .grid(row=0, column=2, padx=10, pady=5, sticky="w")

tk.Checkbutton(muscle_frame, text="Arms (Biceps & Triceps)", variable=arms_var,
               font=("Arial", 12), fg="#0B3760", bg="#B6CDD9", selectcolor="#B6CDD9")\
               .grid(row=1, column=0, padx=10, pady=5, sticky="w")
tk.Checkbutton(muscle_frame, text="Core (Abs & Obliques)", variable=core_var,
               font=("Arial", 12), fg="#0B3760", bg="#B6CDD9", selectcolor="#B6CDD9")\
               .grid(row=1, column=1, padx=10, pady=5, sticky="w")

def generate_workout():
    
    gender = gender_var.get()

    age = age_var.get()
   
    goals = []
    if lose_weight_var.get(): goals.append("Lose Weight")
    if gain_strength_var.get(): goals.append("Gain Strength")
    if gain_muscle_var.get(): goals.append("Gain Muscle")
    if improve_endurance_var.get(): goals.append("Improve Endurance")
    if improve_flexibility_var.get(): goals.append("Increase Flexibility")
    if boost_fitness_var.get(): goals.append("Boost Overall Fitness")
    
    
    level = level_var.get()  
    

    equipment = []
    if barbell_var.get(): equipment.append("Barbell")
    if dumbbells_var.get(): equipment.append("Dumbbells")
    if bodyweight_var.get(): equipment.append("Body Weight")
    if machine_var.get(): equipment.append("Machine")
    if kettlebells_var.get(): equipment.append("Kettlebells")
    if cables_var.get(): equipment.append("Cables")
    if band_var.get(): equipment.append("Band")
    
    
    muscle_workouts = []
    if chest_var.get(): muscle_workouts.append("Chest:\n- Push-ups (3x12)\n- Dumbbell Press (3x10)")
    if back_var.get(): muscle_workouts.append("Back:\n- Pull-ups (3x8)\n- Bent-over Rows (3x10)")
    if legs_var.get(): muscle_workouts.append("Legs:\n- Squats (3x15)\n- Lunges (3x12)")
    if arms_var.get(): muscle_workouts.append("Arms:\n- Bicep Curls (3x12)\n- Tricep Dips (3x10)")
    if core_var.get(): muscle_workouts.append("Core:\n- Plank (3x30s)\n- Crunches (3x15)")

   
    if not gender or not age or not goals or not level or not equipment or not muscle_workouts:
        result_label.config(text="Please make sure you select an option for EVERY section!")
        return

  
    workout_text = f"YOUR CUSTOM WORKOUT PLAN\n\n"
    workout_text += f"1) Gender: {gender}\n"
    workout_text += f"2) Age: {age}\n"
    workout_text += f"3) Fitness Goals: {', '.join(goals)}\n"
    workout_text += f"4) Fitness Level: {level}\n"
    workout_text += f"5) Equipment: {', '.join(equipment)}\n"
    workout_text += f"6) Exercises for Selected Muscle Groups:\n\n"
    workout_text += "\n\n".join(muscle_workouts)

   
    if level == "Beginner":
        workout_text += "\n\nRest: 60 seconds between sets"
    elif level == "Intermediate":
        workout_text += "\n\nRest: 45 seconds between sets"
    elif level == "Advanced":
        workout_text += "\n\nRest: 30 seconds between sets"

    result_label.config(text=workout_text)


generate_button = tk.Button(scrollable_frame,
                            text="Generate Workout Plan Below",
                            font=("Arial", 12, "bold"),
                            fg="white",
                            bg="#0B3760",
                            padx=20,
                            pady=10,
                            command=generate_workout)

generate_button.pack(pady=25)


result_label = tk.Label(scrollable_frame,
                        text="",
                        font=("Arial", 12),
                        fg="#0B3760",
                        bg="#B6CDD9",
                        justify="left")

result_label.pack(pady=10)


root.mainloop()

