_base_ = [
    '../_base_/models/deeplabv3plus_r50-d8_boundary_loss.py', '../_base_/datasets/vaihingen_600.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_80k.py'
]
model = dict(
    decode_head=dict(num_classes=5), auxiliary_head=dict(num_classes=5))
test_cfg = dict(mode='whole')