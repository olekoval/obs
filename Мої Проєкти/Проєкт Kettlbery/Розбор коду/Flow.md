GET /plans/new
  └─ форма створення плану (назва, дата, статус)
       ↓ POST /plans/new
         └─ створює WorkoutPlan → redirect

GET /plans/<id>/edit
  └─ показує план + список вже доданих вправ
     + форма "Додати вправу" (вправа, вага, підходи, повтори, відпочинок)
          ↓ POST /plans/<id>/add-set
            └─ створює WorkoutPlanSet → redirect назад на /plans/<id>/edit

GET /plans/<id>/edit  ← та сама сторінка, вже з новою вправою в списку
  └─ знову форма "Додати вправу"
       ↓ POST /plans/<id>/add-set
         └─ ...і так далі