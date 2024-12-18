#include "pico/stdlib.h"

uint i=0;
void setup() {
    Serial.begin(115200);
    Serial.println("GPIO init");
    for(i=0;i<30;i++)
    {
        gpio_init(i);
        gpio_set_dir(i, GPIO_OUT);
    }
}
void loop() {
    while (true) {
      Serial.println("GPIO HIGH");
      for(i=0;i<30;i++)
      {
          gpio_put(i, 1);
      }
      sleep_ms(2000);
      Serial.println("GPIO LOW");  
      for(i=0;i<30;i++)
      {
          gpio_put(i, 0);
      }
      sleep_ms(2000);
    }
}
