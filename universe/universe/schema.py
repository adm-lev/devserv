import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType
from todos.models import User, Project, Todo


# class Query(ObjectType):
#     hello = graphene.String(default_value='HI!')
# schema = graphene.Schema(query=Query)

# -------------------------------------------------------------------------

# class UserType(DjangoObjectType):
#     class Meta:
#         model = User
#         fields = '__all__'


# class Query(ObjectType):
#     all_users = graphene.List(UserType)

#     def resolve_all_users(root, info):
#         return User.objects.all()

# schema = graphene.Schema(query=Query)


# ----------------------------------------------------------------------


# class UserType(DjangoObjectType):
#     class Meta:
#         model = User
#         fields = '__all__'


# class ProjectType(DjangoObjectType):
#     class Meta:
#         model = Project
#         fields = '__all__'


# class TodoType(DjangoObjectType):
#     class Meta:
#         model = Todo
#         fields = '__all__'


# class Query(ObjectType):
#     all_users = graphene.List(UserType)
#     all_projects = graphene.List(ProjectType)
#     all_todos = graphene.List(TodoType)

#     def resolve_all_users(root, info):
#         return User.objects.all()
    
#     def resolve_all_projects(root, info):
#         return Project.objects.all()

#     def resolve_all_todos(root, info):
#         return Todo.objects.all()

# schema = graphene.Schema(query=Query)


# ---------------------------------------------------------------------------------------


# class UserType(DjangoObjectType):
#     class Meta:
#         model = User
#         fields = '__all__'


# class ProjectType(DjangoObjectType):
#     class Meta:
#         model = Project
#         fields = '__all__'


# class TodoType(DjangoObjectType):
#     class Meta:
#         model = Todo
#         fields = '__all__'


# class Query(ObjectType):
#     all_users = graphene.List(UserType)
#     all_projects = graphene.List(ProjectType)
#     all_todos = graphene.List(TodoType)

#     user_by_id = graphene.List(UserType, id=graphene.Int(required=False))

#     def resolve_user_by_id(root, info, id=None):
#         if id:
#             return User.objects.get(id=id)
#         return User.objects.all()

#     project_by_user = graphene.List(ProjectType, users=graphene.String(required=False))

#     def resolve_project_by_user(root, info, users=None):
#         if users:
#             return Project.objects.filter(users=users)
#         return Project.objects.all()

# schema = graphene.Schema(query=Query)

# --------------------------------------------------------------------------

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class UserDeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    users = graphene.List(UserType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        user = User.objects.get(id=kwargs.get('id')).delete()
        return cls(users=User.objects.all())


class UserUpdateMutation(graphene.Mutation):
    class Arguments:
        user_name = graphene.String(required=True)
        id = graphene.ID()

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        user = User.objects.get(id=kwargs.get('id'))
        user.user_name = kwargs.get('user_name')
        user.save()
        return cls(user=user)


class UserCreateMutation(graphene.Mutation):
    class Arguments:
        user_name = graphene.String(required=True)
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String(required=True)

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        user = User.objects.create(**kwargs)
        return cls(user=user)



class Mutations(ObjectType):
  
    create_user = UserCreateMutation.Field()
    update_user = UserUpdateMutation.Field()
    delete_user = UserDeleteMutation.Field()



class Query(ObjectType):
    hello = graphene.String(default_value='HI!')
    

schema = graphene.Schema(query=Query, mutation=Mutations)









