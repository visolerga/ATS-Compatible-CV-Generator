# app/services/job_service.py

from app.models import Job
from peewee import DoesNotExist

class JobService:
    @staticmethod
    def create_job(user_id, company, role, start_date, end_date=None, description=None):
        """Crea un nuevo trabajo asociado a un usuario."""
        job = Job.create(
            user_id=user_id,
            company=company,
            role=role,
            start_date=start_date,
            end_date=end_date,
            description=description
        )
        return job

    @staticmethod
    def get_job_by_id(job_id):
        """Obtiene un trabajo por su ID."""
        try:
            return Job.get(Job.id == job_id)
        except DoesNotExist:
            return None

    @staticmethod
    def update_job(job_id, **kwargs):
        """Actualiza la información de un trabajo existente."""
        job = JobService.get_job_by_id(job_id)
        if job:
            for key, value in kwargs.items():
                setattr(job, key, value)
            job.save()
            return job
        return None

    @staticmethod
    def delete_job(job_id):
        """Elimina un trabajo de la base de datos."""
        job = JobService.get_job_by_id(job_id)
        if job:
            job.delete_instance()
            return True
        return False
