"""Three built in tiers: Basic, Premium and Enterprise. Created after database migration."""

BUILTIN_TIERS = {
    'Basic': dict(
        thumbnail_size=dict(width=200, height=200),
        is_original_file=False,
        is_expiring_link=False,
    ),
    'Premium': dict(
        thumbnail_size=dict(width=200, height=400),
        is_original_file=True,
        is_expiring_link=False,
    ),
    'Enterprise': dict(
        is_original_file=True,
        is_expiring_link=True,
    ),
}
