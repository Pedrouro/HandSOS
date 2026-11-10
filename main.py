import cv2 as cv
import mediapipe as mp


def main():
    camera = cv.VideoCapture(0)

    while True:
        var, frame = camera.read()

        if not var:
            print("Camera nao encontrada... Fechando programa.")
            break

        frame = cv.flip(frame, 1)

        recordVideo('XVID', frame, 640, 480, 'videoGravado.avi')
        
        cv.imshow('Aperte Q para sair', frame)

        if cv.waitKey(1) == ord('q'):
            break

def recordVideo(videoFormat, camera, X, Y, nomeArquivo):

    fourcc = cv.VideoWriter_fourcc(*f'{videoFormat}')
    out = cv.VideoWriter(f'{nomeArquivo}', fourcc, 20.0, (X,  Y))
    out.write(camera)


if __name__ == "__main__":
    main()