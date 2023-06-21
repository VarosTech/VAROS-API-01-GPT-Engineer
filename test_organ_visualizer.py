from organ_visualizer import OrganVisualizer, PyDicomHandler
from organ_visualizer import FlaskAPI
import vtk
import pytest

def test_organ_visualizer_init():
    ov = OrganVisualizer()
    assert isinstance(ov, OrganVisualizer)

def test_organ_visualizer_parse_description():
    ov = OrganVisualizer()
    organ_name, organ_features = ov.parse_description("healthy heart")
    assert organ_name == "heart"
    assert organ_features == {}

def test_organ_visualizer_generate_visualization():
    ov = OrganVisualizer()
    organ_name, organ_features = ov.parse_description("healthy heart")
    vtk_image = ov.generate_visualization(organ_name, organ_features)
    assert isinstance(vtk_image, vtk.vtkImageData)

def test_organ_visualizer_convert_to_bytes():
    ov = OrganVisualizer()
    organ_name, organ_features = ov.parse_description("healthy heart")
    vtk_image = ov.generate_visualization(organ_name, organ_features)
    bytes_image = ov.convert_to_bytes(vtk_image)
    assert isinstance(bytes_image, bytes)

def test_organ_visualizer_visualize_organ():
    ov = OrganVisualizer()
    bytes_image = ov.visualize_organ("healthy heart")
    assert isinstance(bytes_image, bytes)

def test_pydicom_handler_load_dicom_image():
    ph = PyDicomHandler()
    vtk_image = ph.load_dicom_image("test.dcm")
    assert isinstance(vtk_image, vtk.vtkImageData)

def test_pydicom_handler_process_dicom_image():
    ph = PyDicomHandler()
    vtk_image = ph.load_dicom_image("test.dcm")
    processed_image = ph.process_dicom_image(vtk_image)
    assert isinstance(processed_image, vtk.vtkImageData)

def test_flask_api_visualize_organ():
    ov = OrganVisualizer()
    api = FlaskAPI(ov)
    with api.app.test_client() as client:
        response = client.post('/visualize_organ', json={"organ_description": "healthy heart"})
        assert response.status_code == 200
        assert response.mimetype == "image/jpeg"  # Expect a JPEG image
        assert isinstance(response.data, bytes)

