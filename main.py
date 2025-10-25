import cv2, random, math
import cvzone
from cvzone.HandTrackingModule import HandDetector

# --- Setup camera ---
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
detector = HandDetector(detectionCon=0.8, maxHands=1)

# --- Load bee image ---
bee_img = cv2.imread("bee.png", cv2.IMREAD_UNCHANGED)
if bee_img is None:
    print(" Error: bee.png not found!")
    exit()
bee_img = cv2.resize(bee_img, (80, 80))

# --- Initial positions ---
points = [[random.randint(50, 590), random.randint(50, 430)] for _ in range(3)]
bees = [[random.randint(50, 590), random.randint(50, 430)] for _ in range(2)]

# --- Speeds ---
p_speeds = [[random.choice([-3, 3]), random.choice([-3, 3])] for _ in range(len(points))]
b_speeds = [[random.choice([-4, 4]), random.choice([-4, 4])] for _ in range(len(bees))]

score = 0
game_over = False

while True:
    success, img = cap.read()
    if not success:
        break
    img = cv2.flip(img, 1)

    if not game_over:
        # --- Hand detection ---
        hands, img = detector.findHands(img, draw=False)
        hand_x = hand_y = None
        if hands:
            lmList = hands[0]['lmList']
            hand_x, hand_y = lmList[8][0], lmList[8][1]  # index tip
            cv2.circle(img, (hand_x, hand_y), 8, (255, 0, 0), -1)

        # --- Move and draw points ---
        for i, (px, py) in enumerate(points):
            vx, vy = p_speeds[i]
            px += vx
            py += vy
            if px <= 0 or px >= 640:
                vx *= -1
            if py <= 0 or py >= 480:
                vy *= -1
            points[i] = [px, py]
            p_speeds[i] = [vx, vy]
            cv2.circle(img, (px, py), 15, (0, 255, 0), -1)

            # --- Collision with point (increase score) ---
            if hand_x is not None:
                dist = math.hypot(hand_x - px, hand_y - py)
                if dist < 25:
                    score += 1
                    # Move point to new random position
                    points[i] = [random.randint(50, 590), random.randint(50, 430)]

        # --- Move and draw bees ---
        for i, (bx, by) in enumerate(bees):
            vx, vy = b_speeds[i]
            bx += vx
            by += vy
            if bx <= 0 or bx + 80 >= 640:
                vx *= -1
            if by <= 0 or by + 80 >= 480:
                vy *= -1
            bees[i] = [bx, by]
            b_speeds[i] = [vx, vy]

            # Draw bee image
            img = cvzone.overlayPNG(img, bee_img, [bx, by])

            # --- Collision with bee (game over) ---
            if hand_x is not None:
                dist = math.hypot(hand_x - (bx + 40), hand_y - (by + 40))
                if dist < 40:
                    game_over = True

        # --- Show score ---
        cv2.putText(img, f"Score: {score}", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
        cv2.putText(img, "Avoid the Bees! 🐝", (350, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)

    else:
        cv2.putText(img, "GAME OVER!", (180, 250),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)
        cv2.putText(img, f"Final Score: {score}", (220, 320),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)
        cv2.putText(img, "Press 'R' to Restart or 'Q' to Quit",
                    (100, 370), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

    cv2.imshow("🐝 Hand vs Bees Game", img)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    if key == ord('r'):
        # Reset game
        game_over = False
        score = 0
        points = [[random.randint(50, 590), random.randint(50, 430)] for _ in range(3)]
        bees = [[random.randint(50, 590), random.randint(50, 430)] for _ in range(2)]

cap.release()
cv2.destroyAllWindows()
