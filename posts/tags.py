from database.database import db, Tag

def list_tags():
    tags = Tag.query.all()


    print('tags', tags)
    return tags

def add_tags_to_post(post, tags):

    for tag_name in tags:

        tag = Tag.query.filter_by(name=tag_name).first()

        if not tag:
            tag = Tag(tag_name)

        post.tags.append(tag)

    return True
