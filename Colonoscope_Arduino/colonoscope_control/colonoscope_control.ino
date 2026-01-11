#define STEP_PIN 33
#define DIR_PIN 32


// how many motor steps per key press
const int STEPS_PER_PRESS = 10000;   // Big move per press


// angle per motor step so that each key press ≈ 30°
const float DEGREES_PER_STEP = 30.0f / STEPS_PER_PRESS;


long rotateAmountUD = 0;  // stores motor steps
long rotateAmountLR = 0;  // stores motor steps


// doSteps() 
// Sends a "pulse train" to the stepper driver. 
// One HIGH + one LOW = 1 motor microstep.
void doSteps(int steps) {
  for (int i = 0; i < steps; i++) {
    digitalWrite(STEP_PIN, HIGH);
    delayMicroseconds(100);  // Controls speed of rotation
    digitalWrite(STEP_PIN, LOW);
    delayMicroseconds(100);
  }
}


// Set up pins and serial monitor
void setup() {
  pinMode(STEP_PIN, OUTPUT);
  pinMode(DIR_PIN, OUTPUT);


  Serial.begin(115200);
  Serial.println("WASD to move | R to reset angles");
}


void loop() {
  if (Serial.available()) {
    char key = Serial.read();


  // Ignore newline/return characters
    if (key == '\n' || key == '\r') return;
  
      // D → Down bend
    if (key == 'd' || key == 'D') {
      digitalWrite(DIR_PIN, HIGH);      
      doSteps(STEPS_PER_PRESS);      
      rotateAmountLR += STEPS_PER_PRESS;
    }
  // A → Upward bend
    if (key == 'a' || key == 'A') {
      digitalWrite(DIR_PIN, LOW);
      doSteps(STEPS_PER_PRESS);
      rotateAmountLR -= STEPS_PER_PRESS;
    }


    // reset
    if (key == 'r' || key == 'R') {
      // undo UD
      if (rotateAmountUD != 0) {
        digitalWrite(DIR_PIN, (rotateAmountUD > 0) ? LOW : HIGH);
        doSteps(abs(rotateAmountUD));
        rotateAmountUD = 0;
      }


      // undo LR
      if (rotateAmountLR != 0) {
        digitalWrite(DIR_PIN, (rotateAmountLR > 0) ? LOW : HIGH);
        doSteps(abs(rotateAmountLR));
        rotateAmountLR = 0;
      }


      Serial.println("RESET → All angles set to zero");
    }


    // angle per motor step
    float angleLR = rotateAmountLR * DEGREES_PER_STEP;
    float angleUD = rotateAmountUD * DEGREES_PER_STEP;


    // display angle on serial monitor
    Serial.print("LR Angle: "); Serial.print(angleLR);
    Serial.print(" | UD Angle: "); Serial.println(angleUD);
  }
}
