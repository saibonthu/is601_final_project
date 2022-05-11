import io
import logging


def test_csv_upload(client):
    log = logging.getLogger("csvUploads")
    file_name = "fake-text-stream.csv"
    data = {
        'image': (io.BytesIO(b"some initial text data"), file_name)
    }
    response = client.post('/songs/upload', data=data)
    log.info('csv file upload test!')
    assert response.status_code == 404