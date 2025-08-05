import speedtest as st

### Instalar librería:    pip install speedtest-cli

def Speed_Test():
        test = st.Speedtest()

        download_speed = test.download() / 1_000_000  # Convert to Mbps
        print(f'Download Speed: {download_speed:.2f} Mbps')
        
        upload_speed = test.upload() / 1_000_000  # Convert to Mbps
        print(f'Upload Speed: {upload_speed:.2f} Mbps')
        
        ping = test.results.ping
        print(f'Ping: {ping} ms')


if __name__ == "__main__":
    Speed_Test()
