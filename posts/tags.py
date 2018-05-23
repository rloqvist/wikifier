from database.database import db, Tag, tags

def list_tags():
    tags = Tag.query.all()
    return tags

def list_tags_with_count():
    all_tags = Tag.query.all()

    for tag in all_tags:
        tag_records = db.session.query(tags).filter_by(tag_id=tag.id).all()
        count = len(tag_records)
        tag.count = count

    return sorted(all_tags, key=lambda x: x.count)[::-1]


def add_tags_to_post(post, tags):

    for tag_name in tags:

        tag = Tag.query.filter_by(name=tag_name).first()

        if not tag:
            tag = Tag(tag_name)

        post.tags.append(tag)

    return True
