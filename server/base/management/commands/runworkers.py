from multiprocessing import Process
import yaml
from django.core.management.base import BaseCommand
from zentral.core.queues.workers import get_workers


class Command(BaseCommand):
    help = 'Run Zentral workers.'

    def add_arguments(self, parser):
        parser.add_argument('--list-workers', action='store_true', dest='list_workers', default=False,
                            help='list workers')
        parser.add_argument("--prometheus-base-port", type=int, default=9900)
        parser.add_argument("--prometheus-sd-file")
        parser.add_argument("--external-hostname", default="localhost")
        parser.add_argument("worker", nargs="*")

    def handle(self, *args, **kwargs):
        processes = []
        prometheus_targets = []
        list_workers = kwargs['list_workers']
        prometheus_base_port = kwargs['prometheus_base_port']
        prometheus_sd_file = kwargs.get('prometheus_sd_file')
        external_hostname = kwargs['external_hostname']
        workers = kwargs['worker']
        for idx, worker in enumerate(sorted(get_workers(), key=lambda w: w.name)):
            if list_workers:
                print("Worker '{}'".format(worker.name))
                continue
            elif workers and worker.name not in workers:
                continue
            prometheus_port = prometheus_base_port + idx
            p = Process(target=worker.run,
                        kwargs={"prometheus_port": prometheus_port},
                        name=worker.name)
            p.daemon = 1
            p.start()
            processes.append(p)
            prometheus_targets.append({
                "targets": ["{}:{}".format(external_hostname, prometheus_port)],
                "labels": {"job": worker.name}
            })
        if prometheus_sd_file:
            with open(prometheus_sd_file, "w") as f:
                yaml.dump(prometheus_targets, f, allow_unicode=True)
        for p in processes:
            p.join()
