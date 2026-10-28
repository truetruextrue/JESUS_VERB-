CREATE TABLE IF NOT EXISTS kobllux_interactions (
    event_id UUID PRIMARY KEY,
    occurred_at TIMESTAMPTZ NOT NULL,
    source TEXT NOT NULL CHECK (source IN ('sumbus-fusion/hypervision', 'github-actions')),
    archetypes TEXT[] NOT NULL,
    tags TEXT[] NOT NULL DEFAULT '{}',
    payload JSONB NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS kobllux_interactions_occurred_at_idx
    ON kobllux_interactions (occurred_at DESC);

CREATE INDEX IF NOT EXISTS kobllux_interactions_source_idx
    ON kobllux_interactions (source, occurred_at DESC);

CREATE INDEX IF NOT EXISTS kobllux_interactions_archetypes_idx
    ON kobllux_interactions USING GIN (archetypes);

CREATE INDEX IF NOT EXISTS kobllux_interactions_tags_idx
    ON kobllux_interactions USING GIN (tags);
