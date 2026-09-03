from client import CrossCodebaseApiMigrationImpactMapperClient

def main():
    client = CrossCodebaseApiMigrationImpactMapperClient()
    res = client.map_api_migration_impact('v1_auth()', 'v2_auth()', ['service-a'])
    print('Cross-Codebase Migration Impact Mapper: ' + res['impact_map_id'])
    print('Occurrences: ' + str(res['code_occurrences_found_count']) + ' across ' + str(res['impacted_repositories_count']) + ' repos')
    print('Playbook [1]: ' + res['migration_playbook_steps'][0])
    print('Roadmap URL: ' + res['migration_roadmap_url'])

if __name__ == '__main__':
    main()
