import sounddevice as sd
import numpy as np

def play_tone(frequency, duration=1.0, sample_rate=44100):
    """Generate and play a tone of a given frequency."""
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    sd.play(wave, samplerate=sample_rate, loop=True)

print("Generador de sonido: Ingresa la frecuencia en Hz (Ctrl + C para detener).")

try:
    while True:
        user_input = input("Frecuencia (Hz): ")
        try:
            frequency = float(user_input)
            if frequency <= 0:
                print("Por favor, ingresa un número positivo.")
                continue
            print(f"Reproduciendo sonido a {frequency} Hz. Presiona Ctrl + C para detener.")
            play_tone(frequency)
            input("Presiona Enter para detener el sonido.")
            sd.stop()
        except ValueError:
            print("Por favor, ingresa un número válido.")
except KeyboardInterrupt:
    print("\nPrograma terminado.")
    sd.stop()



# Example Usage:
generator = FrequencyGenerator()
generator.start()


while True:
    try:
        new_frequency = int(input("Enter new frequency (or 'q' to quit): "))
        generator.set_frequency(new_frequency)
    except ValueError:
        print("Invalid input. Please enter a number or 'q'.")
    except KeyboardInterrupt: # Ctrl-C to exit cleanly
        break
    except Exception as e:
        print(f"An error occurred: {e}")

generator.stop()

print("Exiting...")

