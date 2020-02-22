docker build -t freemenbot . --network=host
docker run -itd --network=host freemenbot
