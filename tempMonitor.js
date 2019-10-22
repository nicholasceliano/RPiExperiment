var sensorLib = require("node-dht-sensor");

var app = {
    sensors: [
      {
        name: "Indoor",
        type: 11,
        pin: 22
      }
    ],
    read: function() {
      for (var sensor in this.sensors) {
        var readout = sensorLib.read(
          this.sensors[sensor].type,
          this.sensors[sensor].pin
        );

        const tempFarenheit = (readout.temperature.toFixed(1) * 9/5) + 32;

        console.log(
          `[${this.sensors[sensor].name}] ` +
            `temperature: ${tempFarenheit}°F, ` +
            `humidity: ${readout.humidity.toFixed(1)}%`
        );
      }
      setTimeout(function() {
        app.read();
      }, 2000);
    }
  };
   
  app.read();