import json
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from core.models import PatientProfile, PatientDiagnosisReadings, PatientDiagnosisList, PatientLabResult


class DiagnosisSerializer(ModelSerializer):
    blood_pressure = serializers.SerializerMethodField()
    heart_rate = serializers.SerializerMethodField()
    respiratory_rate = serializers.SerializerMethodField()
    temperature = serializers.SerializerMethodField()

    def get_blood_pressure(self, instance):
        blood_pressure = json.loads(instance.blood_pressure)['blood_pressure']
        return {k:blood_pressure[k] for k in blood_pressure}
    
    def get_heart_rate(self, instance):
        heart_rate = json.loads(instance.heart_rate)['heart_rate']
        return {k:heart_rate[k] for k in heart_rate}
    
    def get_respiratory_rate(self, instance):
        respiratory_rate = json.loads(instance.respiratory_rate)['respiratory_rate']
        return {k:respiratory_rate[k] for k in respiratory_rate}

    def get_temperature(self, instance):
        temperature = json.loads(instance.temperature)['temperature']
        return {k:temperature[k] for k in temperature}

    class Meta:
        model = PatientDiagnosisReadings
        fields = [
            'month', 'year', 'blood_pressure', 'heart_rate', 'respiratory_rate', 'temperature'
        ]


class DiagnosisListSerializer(ModelSerializer):
    class Meta:
        model = PatientDiagnosisList
        fields = [
            'name', 'description', 'status'
        ]


class LabResultsSerializer(ModelSerializer):
    class Meta:
        model = PatientLabResult
        fields = [
            'lab_result'
        ]

    
class UserDetailsSerializer(ModelSerializer):
    diagnosis_history = DiagnosisSerializer(many=True, source='patientdiagnosisreadings_set')

    diagnosis_list = DiagnosisListSerializer(many=True, source='patientdiagnosislist_set')

    lab_results = serializers.SerializerMethodField()

    def get_lab_results(self, instance):
        return [obj.lab_result for obj in instance.patientlabresult_set.all()]
    
    class Meta:
        model = PatientProfile
        fields = [
            'id', 'name', 'gender', 'age', 'profile_picture', 'date_of_birth', 'phone_number', 'emergency_contact', 'insurance_type', 'diagnosis_history', 'diagnosis_list', 'lab_results'
        ]


class PatientsProfileSerializer(ModelSerializer):
    class Meta:
        model = PatientProfile
        fields = [
            'id', 'name', 'gender', 'age', 'profile_picture'
        ]