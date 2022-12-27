import pytest
from rest_framework.test import APIClient
from model_bakery import baker 

from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory 


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_retrieve_course(client, course_factory):
    test_course = course_factory(_quantity=1)

    response = client.get(f'/api/v1/courses/{test_course[0].id}/')
    data = response.json()

    assert response.status_code == 200
    assert data['id'] == test_course[0].id
    assert data['name'] == test_course[0].name


@pytest.mark.django_db
def test_list_courses(client, course_factory):
    test_courses = course_factory(_quantity=5)

    response = client.get('/api/v1/courses/')
    data = response.json()

    assert response.status_code == 200
    for i, course in enumerate(data):
        assert course['name'] == test_courses[i].name


@pytest.mark.django_db
def test_filter_by_id(client, course_factory):
    test_courses = course_factory(_quantity=5)

    response = client.get('/api/v1/courses/', {'id': test_courses[3].id})
    data = response.json()

    assert response.status_code == 200
    assert data[0]['id'] == test_courses[3].id
    assert data[0]['name'] == test_courses[3].name


@pytest.mark.django_db
def test_filter_by_name(client, course_factory):
    test_courses = course_factory(_quantity=5)

    response = client.get('/api/v1/courses/', {'name': test_courses[2].name})
    data = response.json()

    assert response.status_code == 200
    assert data[0]['id'] == test_courses[2].id
    assert data[0]['name'] == test_courses[2].name


@pytest.mark.django_db
def test_create_course(client):
    course = {'name': 'test course'}

    response = client.post('/api/v1/courses/', data=course)
    request = client.get('/api/v1/courses/', {'name': course['name']})

    assert response.status_code == 201
    assert request.status_code == 200


@pytest.mark.django_db
def test_update_course(client, course_factory):
    test_course = course_factory(_quantity=1)
    update = {'name': 'new name'}

    response = client.patch(f'/api/v1/courses/{test_course[0].id}/', data=update)
    data = response.json()

    assert response.status_code == 200
    assert data['name'] == update['name']


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    test_course = course_factory(_quantity=1)

    response = client.delete(f'/api/v1/courses/{test_course[0].id}/')
    request = client.get(f'/api/v1/courses/{test_course[0].id}/')
    
    assert response.status_code == 204
    assert request.status_code == 404