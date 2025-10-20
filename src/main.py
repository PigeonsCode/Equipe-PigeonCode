import sys
import os
sys.path.append(os.path.dirname(__file__))

from projeto import app 
if __name__ == "__main__":
    app.run(debug=True)