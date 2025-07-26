echo "Starting main.sh"
echo "Starting main.py"
python /home/heinrich/workspace/StaticSite/src/main.py
echo "cd public performed"
cd public
echo "Server started"
python3 -m http.server 8888 #&
#sleep 10
# Potentially add commands to stop the server after test
#pkill -f "http.server"